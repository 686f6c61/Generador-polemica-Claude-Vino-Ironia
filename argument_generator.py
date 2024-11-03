import os
import random
import time
import json
import re
from anthropic import Anthropic, APIError, APITimeoutError, RateLimitError
from translate import Translator
from dotenv import load_dotenv

load_dotenv()

class ChristmasArgumentGenerator:
    """
    Generador de argumentos navideños usando la API de Anthropic Claude.
    Genera argumentos provocadores y maridajes de vino irónicos.
    """
    
    # Constantes para el manejo de reintentos
    MAX_RETRIES = 3
    RETRY_DELAY = 2

    # Niveles de intensidad predefinidos para los argumentos
    INTENSITY_LEVELS = {
        "suave": "mantén un tono amigable y casual, usando ejemplos cotidianos y experiencias personales con humor ligero",
        "moderada": "usa un tono más apasionado pero respetuoso, con ejemplos más específicos y experiencias personales convincentes",
        "intensa": "emplea un tono muy apasionado y dramático, con ejemplos impactantes y experiencias personales emotivas"
    }

    def __init__(self):
        """Inicializa el generador con la API key de Anthropic y el traductor."""
        api_key = os.environ.get("ANTHROPIC_API_KEY")
        if not api_key:
            raise ValueError("ANTHROPIC_API_KEY no está configurada en las variables de entorno")
        self.anthropic = Anthropic(api_key=api_key)
        self.translator = Translator(to_lang="es")
        
    def translate_text(self, text):
        """Traduce texto a español usando el servicio de traducción."""
        try:
            return self.translator.translate(text)
        except Exception as e:
            print(f"Error de traducción: {e}")
            return text

    def verify_unique_arguments(self, arguments):
        """Verifica que los argumentos generados sean únicos."""
        argument_texts = [arg['argument'].lower() for arg in arguments]
        return len(set(argument_texts)) == len(argument_texts)

    def generate_argument(self, target_person, topic, intensity, position):
        """
        Genera argumentos personalizados usando la API de Claude.
        
        Args:
            target_person (str): Persona con quien se debatirá
            topic (str): Tema del debate
            intensity (str): Nivel de intensidad del argumento
            position (str): Posición a favor o en contra
            
        Returns:
            dict: JSON con argumentos y maridajes generados
        """
        print(f"Starting argument generation for {target_person} about {topic} with {intensity} intensity...")
        
        # Configuración de intensidad y posición
        intensity_instruction = self.INTENSITY_LEVELS.get(intensity.lower(), self.INTENSITY_LEVELS["moderada"])
        position_text = "a favor" if position == "favor" else "en contra"
        
        # Prompt mejorado para Claude
        prompt = f"""Como Profesor de Filosofía, genera 5 argumentos {position_text} de {topic} para debatir con {target_person}.
        La intensidad debe ser {intensity} ({intensity_instruction}).
        
        Cada argumento debe:
        1. Ser una frase completa y coherente
        2. Incluir una conclusión clara
        3. Adaptarse al nivel de intensidad especificado
        4. Mantener la posición {position_text} del tema
        5. Incluir un maridaje de vino irónico relacionado
        
        Responde en formato JSON con esta estructura:
        {{
            "arguments": [
                {{
                    "topic": "subtema específico",
                    "argument": "argumento completo",
                    "wine": "nombre del vino",
                    "wine_reason": "razón irónica del maridaje"
                }}
            ]
        }}
        """

        # Intentos de generación con reintentos en caso de error
        for attempt in range(self.MAX_RETRIES):
            try:
                print(f"Attempt {attempt + 1} to generate arguments...")
                # Llamada a la API de Claude
                response = self.anthropic.beta.messages.create(
                    model="claude-3-5-sonnet-latest",
                    max_tokens=2000,
                    temperature=0.9,
                    messages=[{"role": "user", "content": prompt}]
                )
                
                print("Claude API Response:", response.content[0].text)
                
                # Procesamiento de la respuesta
                try:
                    content = json.loads(response.content[0].text)
                    if not self.verify_unique_arguments(content['arguments']):
                        print("Generated arguments are not unique enough, retrying...")
                        continue
                    print("Successfully parsed JSON:", json.dumps(content, indent=2, ensure_ascii=False))
                    return content
                except json.JSONDecodeError as je:
                    # Intento de recuperación de JSON malformado
                    print(f"JSON parsing error: {je}")
                    json_match = re.search(r'\{.*\}', response.content[0].text, re.DOTALL)
                    if json_match:
                        content = json.loads(json_match.group())
                        if not self.verify_unique_arguments(content['arguments']):
                            print("Generated arguments are not unique enough, retrying...")
                            continue
                        print("Successfully extracted and parsed JSON:", json.dumps(content, indent=2, ensure_ascii=False))
                        return content
                    else:
                        raise Exception("Could not parse JSON from response")
                
            except (APIError, APITimeoutError, RateLimitError) as e:
                # Manejo de errores de la API
                print(f"API error (attempt {attempt + 1}/{self.MAX_RETRIES}): {e}")
                if attempt < self.MAX_RETRIES - 1:
                    time.sleep(self.RETRY_DELAY * (attempt + 1))
                continue
            except Exception as e:
                print(f"Unexpected error: {e}")
                if attempt < self.MAX_RETRIES - 1:
                    time.sleep(self.RETRY_DELAY * (attempt + 1))
                continue

        # Datos de respaldo en caso de fallo total
        print("All attempts failed, using fallback data...")
        fallback_data = {
            "arguments": [
                {
                    "topic": f"Una experiencia personal con {topic}",
                    "argument": f"Mira {target_person}, te voy a contar algo que me pasó...",
                    "wine": "Rioja Gran Reserva 2015",
                    "wine_reason": "Un vino añejo y tradicional, porque como dicen los abuelos..."
                }
            ] * 5
        }
        return fallback_data
