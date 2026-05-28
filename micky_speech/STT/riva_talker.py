#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import threading
import riva.client
import riva.client.audio_io

class RivaPublisherNode(Node):
    def __init__(self):
        super().__init__('riva_publisher_node')
        self.publisher_ = self.create_publisher(String, 'comandos_voz', 10)
        self.get_logger().info('Nó do Riva ASR iniciado.')

        self.server_uri = "localhost:50051"
        self.auth = riva.client.Auth(uri=self.server_uri)
        self.asr_service = riva.client.ASRService(self.auth)

        self.sample_rate_hz = 16000
        self.config = riva.client.RecognitionConfig(
            encoding=riva.client.AudioEncoding.LINEAR_PCM,
            sample_rate_hertz=self.sample_rate_hz,
            language_code="pt-BR",
            max_alternatives=1,
            enable_automatic_punctuation=False,
            verbatim_transcripts=True,
        )
        
        self.streaming_config = riva.client.StreamingRecognitionConfig(
            config=self.config,
            interim_results=False
        )

        self.riva_thread = threading.Thread(target=self.run_riva_streaming)
        self.riva_thread.daemon = True
        self.riva_thread.start()

    def run_riva_streaming(self):
        with riva.client.audio_io.MicrophoneStream(
            rate=self.sample_rate_hz,
            chunk=self.sample_rate_hz // 10,
            device=None,
        ) as audio_chunk_iterator:
            self.get_logger().info("Microfone ativado! Pode falar.")
            
            responses = self.asr_service.streaming_response_generator(
                audio_chunks=audio_chunk_iterator,
                streaming_config=self.streaming_config,
            )

            for response in responses:
                if not response.results:
                    continue
                result = response.results[0]
                if result.is_final:
                    transcript = result.alternatives[0].transcript.strip()
                    if transcript:
                        msg = String()
                        msg.data = transcript
                        self.publisher_.publish(msg)
                        self.get_logger().info(f'🎙️ Comando publicado: "{msg.data}"')

def main(args=None):
    rclpy.init(args=args)
    node = RivaPublisherNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info('Encerrando...')
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()