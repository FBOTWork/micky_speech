#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
import numpy as np
import sounddevice as sd

from micky_interfaces.srv import SynthesizeSpeech
import riva.client as rclient

class RivaTTSNode(Node):
    def __init__(self):
        super().__init__('riva_tts_node')
        
        # Aponta para o servidor Riva rodando localmente na sua máquina
        self.declare_parameter('riva_url', '10.228.245.233:50051')  # Substitua pelo endereço do seu servidor Riva
        self.declare_parameter('language_code', 'pt-BR')  # Código de idioma padrão
        self.declare_parameter('voice_name', 'Micky')

        riva_url = self.get_parameter('riva_url').get_parameter_value().string_value
        
        try:
            self.auth = rclient.Auth(uri=riva_url)
            self.riva_client = rclient.SpeechSynthesisService(self.auth)
            self.get_logger().info(f"Conectado ao servidor Riva local: {riva_url}")
        except Exception as e:
            self.get_logger().error(f"Falha ao conectar no Riva: {str(e)}")

        self.srv = self.create_service(
            SynthesizeSpeech, 
            '/micky/speech/tts', 
            self.speak_callback
        )
        self.get_logger().info("Serviço /micky/speech/tts (Potuguês) pronto!")

    def speak_callback(self, request, response):
        text_to_speak = request.text
        lang = request.lang if request.lang else self.get_parameter('language_code').value
        voice = self.get_parameter('voice_name').value

        self.get_logger().info(f"Processando fala: '{text_to_speak}' [{lang}]")

        try:
            # Chama o serviço gRPC do Riva
            riva_response = self.riva_client.synthesize(
                text=text_to_speak,
                language_code='en-US',
                voice_name=voice,
                sample_rate_hz=22050
            )
            
            # Converte a resposta e toca o áudio
            audio_data = np.frombuffer(riva_response.audio, dtype=np.int16)
            audio_data = audio_data * 3.0
            audio_data = np.clip(audio_data, -32768, 32767).astype(np.int16)
            sd.play(audio_data, samplerate=22050)
            sd.wait()


            response.success = True
        except Exception as e:
            self.get_logger().error(f"Erro durante a síntese de voz: {str(e)}")
            response.success = False

        return response

def main(args=None):
    rclpy.init(args=args)
    node = RivaTTSNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()