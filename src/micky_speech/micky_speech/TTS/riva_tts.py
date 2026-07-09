#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
import numpy as np
import sounddevice as sd

# Importação da nossa interface recém-criada
from micky_interfaces.srv import SynthesizeSpeech

# Importação do cliente oficial do Riva
import riva.client as rclient

class RivaTTSNode(Node):
    def __init__(self):
        super().__init__('riva_tts_node')
        
        # Configuração dos parâmetros de rede e voz
        self.declare_parameter('riva_url', '192.168.10.2:50051')
        self.declare_parameter('language_code', 'en-US')
        self.declare_parameter('voice_name', 'English-US-Female-1')
        
        riva_url = self.get_parameter('riva_url').get_parameter_value().string_value
        
        # Inicializa o cliente gRPC do Riva
        try:
            # Corrigido para usar rclient e a variável dinâmica do IP
            self.auth = rclient.Auth(uri=riva_url)
            # Corrigido para usar o self.auth
            self.riva_client = rclient.SpeechSynthesisService(self.auth)
            self.get_logger().info(f"Conectado ao servidor Riva na Jetson Orin: {riva_url}")
        except Exception as e:
            self.get_logger().error(f"Falha ao conectar no Riva: {str(e)}")

        # Criação do Serviço ROS 2
        self.srv = self.create_service(
            SynthesizeSpeech, 
            '/micky/speech/tts', 
            self.speak_callback
        )
        self.get_logger().info("Serviço /micky/speech/tts pronto para receber requisições!")

    def speak_callback(self, request, response):
        text_to_speak = request.text
        lang = request.lang if request.lang else self.get_parameter('language_code').value
        voice = self.get_parameter('voice_name').value

        self.get_logger().info(f"Processando fala: '{text_to_speak}' no idioma [{lang}]")

        try:
            # Na biblioteca moderna da NVIDIA, passamos os argumentos direto na chamada
            riva_response = self.riva_client.synthesize(
                text=text_to_speak,
                language_code=lang,
                voice_name=voice,
                sample_rate_hz=22050
            )
            
            # Transforma a resposta binária em áudio para o Python
            audio_data = np.frombuffer(riva_response.audio, dtype=np.int16)

            # Toca o áudio recebido na caixa de som do PC local
            sd.play(audio_data, samplerate=22050)
            sd.wait() # Bloqueia o serviço até o robô terminar de falar fisicamente

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