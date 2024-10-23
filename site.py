<!DOCTYPE html>
<html>
<head>
    <title>juegodereciclajebylio1736288</title>
    <style>
        body {
            text-align: center;
        }
    </style>
</head>
<body>
    <h1>Hola!</h1>
    <p>By lio.</p>
    <h3>__________________________________________________________________________________________________________________________________</h3>
</html>
<!DOCTYPE html>
<html lang="Es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Настройки</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            margin: 50px;
        }
        #settings {
            display: none; /* скрыть настройки по умолчанию */
            border: 1px solid #ccc;
            padding: 20px;
            margin-top: 20px;
            border-radius: 5px;
        }
    </style>
</head>
<body>

    <button id="toggleButton">ABRIR configuración</button>

    <div id="settings">
        <h2>Configuracíon</h2>
        <label for="brightness">brillo:</label>
        <input type="range" id="brightness" min="0" max="100" value="50"><br><br>
        
        <label for="volume">Volumen:</label>
        <input type="range" id="volume" min="0" max="100" value="50">
    </div>

    <script>
        const toggleButton = document.getElementById('toggleButton');
        const settings = document.getElementById('settings');

        toggleButton.addEventListener('click', () => {
            if (settings.style.display === "none" || settings.style.display === "") {
                settings.style.display = "block";
                toggleButton.textContent = "CERRAR configuración";
            } else {
                settings.style.display = "none";
                toggleButton.textContent = "ABRIR configuración";
            }
        });
    </script>

</body>
</html>
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Juego de Reciclaje</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            margin: 50px;
        }
        #question {
            margin: 20px 0;
        }
    </style>
</head>
<body>

    <h1>Juego de Reciclaje</h1>
    <div id="question"></div>
    <button id="yes">Sí</button>
    <button id="no">No</button>
    <button id="restart">juego de nuevo</button>
    
    <p id="result"></p>
    <button id="restart" style="display: none;">Reiniciar juego</button>

    <script>
        const questions = [
            "¿Se puede reciclar el papel?",
            "¿Las botellas de plástico son reciclables?",
            "¿Se puede reciclar el vidrio?",
            "¿El cartón es reciclable?",
            "¿Los pañales se pueden reciclar?",
            "¿Las latas de aluminio son reciclables?",
            "¿El aceite de cocina se puede reciclar?",
            "¿Se pueden reciclar los electrodomésticos?",
            "¿Los residuos orgánicos se pueden reciclar?",
            "¿Las bolsas de plástico son reciclables?",
            "¿El papel de regalo es reciclable?",
            "¿Las cápsulas de café son reciclables?",
            "¿Se pueden reciclar los restos de comida?",
            "¿Las pilas son reciclables?",
            "¿El cristal roto se puede reciclar?",
            "¿Los productos de limpieza son reciclables?",
            "¿Los envases de yogur son reciclables?",
            "¿Las flores secas se pueden reciclar?",
            "¿Los residuos de construcción son reciclables?",
            "¿Las toallas de papel son reciclables?",
            "¿Las botellas de vidrio son reciclables?",
            "¿Los residuos electrónicos se pueden reciclar?",
            "¿Las cajas de pizza son reciclables?",
            "¿El plástico biodegradable se puede reciclar?",
            "¿Las almohadas son reciclables?",
            "¿Las etiquetas de plástico son reciclables?",
            "¿Los restos de jardinería se pueden reciclar?",
            "¿Los cepillos de dientes son reciclables?",
            "¿Las cajas de cereal son reciclables?",
            "¿Las tapas de botellas son reciclables?",
            "¿Los restos de comida animal son reciclables?",
            "¿Las jeringas se pueden reciclar?",
            "¿Las botellas de champú son reciclables?",
            "¿Las bolsas de papel son reciclables?",
            "¿Los muebles viejos se pueden reciclar?",
            "¿Los espejos son reciclables?",
            "¿Los juguetes de plástico son reciclables?",
            "¿Las cajas de medicamentos son reciclables?",
            "¿Las botellas de refresco son reciclables?",
            "¿Los palitos de helado son reciclables?",
            "¿Las cajas de productos congelados son reciclables?",
            "¿Las latas de conserva son reciclables?",
            "¿Las bolsas de tela son reciclables?"
        ];

        const answers = [
            true, true, true, true, false, true,
            false, true, true, false, true, true,
            true, true, true, false, false, true,
            false, true, false, false, true, true,
            false, true, false, false, true, true,
            true, true, true, false, true, false,
            true, true, false, true, true, true,
            true, false, true, true, true, true,
            true, false, true, false, true, true
        ];

        let currentQuestion = 0;
        let score = 0;

        const questionElement = document.getElementById('question');
        const resultElement = document.getElementById('result');
        const restartButton = document.getElementById('restart');

        function displayQuestion() {
            if (currentQuestion < questions.length) {
                questionElement.textContent = questions[currentQuestion];
            } else {
                endGame();
            }
        }

        function endGame() {
            questionElement.style.display = 'none';
            resultElement.textContent = `Juego terminado. Tu puntuación: ${score} de ${questions.length}`;
            restartButton.style.display = 'block';
        }

        document.getElementById('yes').addEventListener('click', function() {
            if (answers[currentQuestion]) score++;
            currentQuestion++;
            displayQuestion();
        });

        document.getElementById('no').addEventListener('click', function() {
            if (!answers[currentQuestion]) score++;
            currentQuestion++;
            displayQuestion();
        });

        restartButton.addEventListener('click', function() {
            currentQuestion = 0;
            score = 0;
            resultElement.textContent = '';
            restartButton.style.display = 'none';
            questionElement.style.display = 'block';
            displayQuestion();
        });

        displayQuestion();

    </script>

</body>
</html>

<body>
  <h1>Informacion de reciclar</h1>
  <p>Claro, aquí tienes la información sobre el reciclaje en español:

1. Qué se puede reciclar:

Papel: periódicos, cartón, papel de oficina.

Plástico: botellas, envases, empaques.

Metal: aluminio, acero, latas.

Vidrio: botellas, tarros, envases.

Residuos electrónicos: teléfonos viejos, computadoras.


2. Ventajas del reciclaje:

Conservación de recursos: reduce la necesidad de nuevas materias primas.

Reducción de la contaminación: disminuye las emisiones de carbono y otras sustancias nocivas.

Ahorro de energía: reciclar consume menos energía que producir nuevos materiales.

Generación de empleo: las empresas de reciclaje crean nuevos puestos de trabajo.


3. Proceso de reciclaje:

Recolección: los residuos se recogen a través de contenedores y programas especiales.

Clasificación: los materiales se clasifican por tipo.

Tratamiento: los materiales reciclables se procesan y preparan para su reutilización.

Producción: a partir de los materiales reciclados se fabrican nuevos productos.


4. Problemas del reciclaje:

Falta de concienciación: muchas personas no saben qué se puede reciclar.

Contaminación: la contaminación de los materiales reciclables (por ejemplo, con restos de comida) reduce su capacidad de reciclaje.

Logística: la complejidad de la recolección y el transporte de residuos.


5. Cómo participar en el reciclaje:

Clasifica los residuos: separa los materiales reciclables de la basura general.

Usa productos reciclados: compra productos fabricados con materiales reciclados.

Educa a los demás: comparte conocimientos sobre el reciclaje con amigos y familiares.


El reciclaje es una parte fundamental del desarrollo sostenible, y cada uno de nosotros puede contribuir a la conservación del planeta. Si necesitas más información sobre aspectos específicos, ¡hazmelo saber!
<em></em>
</p>
</body>

<!DOCTYPE html>
<html lang="es">
<head>
<body>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Información sobre el reciclaje</title>
    <style>
        body {
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            font-family: 'Arial', sans-serif;
            background-color: #e0f7fa;
        }
        header {
            background-color: #00796b;
            color: white;
            padding: 15px;
            border-radius: 8px;
            margin-bottom: 20px;
            text-align: center;
            width: 80%;
        }
        #info {
            display: none;
            margin-top: 20px;
            border: 2px solid #00796b;
            padding: 15px;
            width: 80%;
            background-color: #ffffff;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        }
        button {
            padding: 10px 20px;
            font-size: 16px;
            background-color: #00796b;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            transition: background-color 0