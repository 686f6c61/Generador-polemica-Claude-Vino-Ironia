# 🎄 Generador de polémicas Navideñas con IA e ironía 🍷

Una aplicación web divertida que genera argumentos para debates navideños usando la IA de Claude 3.5 Sonnet, junto con maridajes de vino irónicos para cada argumento.

## 🎯 Características

- Generación de argumentos personalizados según el tema y la persona
- Tres niveles de intensidad en los debates (suave, moderada, intensa)
- Posicionamiento a favor o en contra del tema
- Maridajes de vino irónicos para cada argumento
- Interfaz web intuitiva y responsiva

## 🤖 Tecnología

### Claude 3.5 Sonnet
Utilizamos el último modelo de Anthropic, Claude 3.5 Sonnet, para generar argumentos coherentes y contextualizados. El modelo está entrenado para:
- Mantener un tono apropiado según la intensidad seleccionada
- Generar argumentos únicos y relevantes
- Crear maridajes de vino humorísticos

### Flask
Framework web ligero de Python que proporciona:
- Manejo eficiente de rutas y peticiones
- Sistema de templates Jinja2
- Fácil integración con APIs externas

## 💭 Prompt Engineering

El sistema utiliza un prompt especializado que actúa como un Profesor de Filosofía especializado en teoría de la argumentación:

```
Como Profesor de Filosofía, genera 5 argumentos {position_text} de {topic} para debatir con {target_person}.
La intensidad debe ser {intensity} ({intensity_instruction}).

Cada argumento debe:
1. Ser una frase completa y coherente
2. Incluir una conclusión clara
3. Adaptarse al nivel de intensidad especificado
4. Mantener la posición {position_text} del tema
5. Incluir un maridaje de vino irónico relacionado

Responde en formato JSON con esta estructura:
{
    "arguments": [
        {
            "topic": "subtema específico",
            "argument": "argumento completo",
            "wine": "nombre del vino",
            "wine_reason": "razón irónica del maridaje"
        }
    ]
}
```

### 📊 Estructura de la respuesta

- **topic**: Subtema específico dentro del tema principal
- **argument**: Argumento completo y coherente
- **wine**: Nombre del vino seleccionado para el maridaje
- **wine_reason**: Explicación irónica de por qué ese vino es perfecto para el argumento

### 🎭 Niveles de intensidad

- **Suave**: Tono amigable y casual, con ejemplos cotidianos y humor ligero
- **Moderada**: Tono apasionado pero respetuoso, con ejemplos específicos
- **Intensa**: Tono muy apasionado y dramático, con ejemplos impactantes

## 🚀 Instalación

1. Clona el repositorio:
```
git clone https://github.com/686f6c61/Generador-polemica-Claude-Vino-Ironia.git
```


2. Instala las dependencias:

```
pip install -r requirements.txt
```

3. Configura tu API key de Anthropic en un archivo `.env`:

```
ANTHROPIC_API_KEY=your_anthropic_api_key
```


4. Ejecuta la aplicación:
```
python main.py
```

## 🛠️ Tecnologías utilizadas

- Python 3.8+
- Flask
- Anthropic Claude API
- Bulma CSS
- JavaScript (Vanilla)

## 📝 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE.md](LICENSE.md) para más detalles.

## 🤝 Contribuir

Las contribuciones son bienvenidas. Por favor, abre un issue primero para discutir qué te gustaría cambiar.

## ⚠️ Disclaimer

Esta aplicación está diseñada con fines humorísticos y educativos. Los argumentos generados son simulaciones y no deben tomarse como consejos reales para conflictos familiares.



