# Proyecto_DAAD

<h2>
  <ul>
    <li>VALDES NAVA JAVIER</li>
    <li>TRUJANO ORTÍZ LUÍS ANTONIO</li>
    <li>IVAN URIEL ROSARIO MARGARITO</li>
  </ul>
</h2>

<p>Esta aplicación tiene 2 usos: </p>
<ol>
  <li>Como PyGame (PARA RECABAR DATOS Y ANALIZARLOS)</li>
  <li>Como un analizador de movimientos y probabilidades (SIMILAR LAS TABLAS DE PROBABILIDAD DEL POKER)</li>
</ol>
<p>El PyGame que tiene asociado se llama "El raton y los gatos", se juega en un tablero de Ajedrez y las fichas son precisamente un Raton y 4 Gatos</p>
<h3>INSTRUCCIONES PARA CORRER EL PROGRAMA</h3>

<p>Primero descarga una versión de Python 3 en el siguiente enlace: </p>
<a href = "https://www.python.org/downloads/" target = "_blank"> https://www.python.org/downloads/ </a>
<p>Una vez instalado, debes instalar las librerias de Python</p>
<ul>
  <li>Numpy</li>
  <li>matplotlib</li>
  <li>pandas</li>
  <li>plotly</li>
</ul>
<p>Recomiendo este video para ver como se realiza la instalación (sirve para cualquier sistema operativo)</p>
<a href = "https://www.youtube.com/watch?v=JB0kIqT1BEk" target = "_blank">https://www.youtube.com/watch?v=JB0kIqT1BEk</a>
<p>Una vez que instalamos estas librerias, seguimos los siguientes pasos generales</p> 
<p>(para una explicación más a fondo, recomiendo entrar al directorio</p> 
<a href = "https://github.com/JavierVN009/Proyecto_DAAD/blob/main/file/Proyecto%20-%20Parte%203.pdf" target = "_blank">file archivo 'Proyecto Parte 3.pdf' página 9</a> 
<p>que contiene pasos más desglosados de como correr el programa, esta es una explicación más general)</p>
<h4>P A S O S</h4>
<ol>
  <li>Descarga el repositorio como ZIP (o clonarlo)</li>
  <li>Descomprimirlo en caso de haberlo descargado como ZIP</li>
  <li>Abrir el directorio del proyecto y acto seguido, abrir el directorio que se llama "src"</li>
  <li>Ejecutar en su interprete de Python el archivo de python "Main.py"</li>
  <li>Seguir las instrucciones del Programa tras ejecutarlo</li>
</ol>
<p>Correr la implementación en google Colab o en Jupyter es un poco más complicado, la explicación de como hacerlo utilizando estas herramientas también se encuentra en <a href = "https://github.com/JavierVN009/Proyecto_DAAD/blob/main/file/Proyecto%20-%20Parte%203.pdf" target = "_blank">file archivo 'Proyecto Parte 3.pdf' página 9</a> </p>
<h3>Clases involucradas</h3>
<p>Aunque en el programa solo observes a la clase Main en accion, ciertamente hay muchas más involucradas, y son estas:</p>
<ul>
  <li><b>Ajedrez</b>: Una clase abstracta que Simula un tablero de Ajedrez, tiene 3 atributos y 8 métodos</li>
  <li><b>Raton (hereda de Ajedrez)</b>: Una clase que simula una de las fichas que dennotan el Ratón, tiene los atributos y metodos heredados de Ajedrez, y un metodo extra.</li>
  <li><b>Gato (Hereda de Ajedrez)</b>: Una clase que simula una de las fichas que dennota el Gato, tiene los atributos y métodos heredados de Ajedrez, y 4 metodos extra.</li>
  <li><b>GatoCPU (Hereda de Gato)</b>: Una clase que simula una de las fichas que dennota un Gato que es controlado por la computadora, tiene los atributos y métodos heredados de la clase Gato, y ademas la implementación de un método abstracto para que se mueva por el tablero de Ajedrez.</li>
  <li><b>GatoNOCPU (Hereda de Gato)</b>: Una clase que simula una de las fichas que dennota un Gato que es controlado por otro jugador, tiene los atributos y métodos heredados de la clase Gato, y ademas la implementación de un método abstracto para que se mueva por el tablero de Ajedrez.</li>
</ul>
<p>Dentro de la clase MAIN simplemente se importan a los GatosCPU, el no CPU y el Raton. El Gato y el Ajedrez se mandan a llamar dentro de los archivos de esas clases; se importan como paquetes.</p>
<h3>¿Cómo se hace el Analisis?</h3>
<p>El analisis es de hecho bastante simple, leemos un CSV en el Python, lo convertimos a DataFrame, calculamos probabilidades y las proyectamos como una tabla de resultados y dos gráficos de barras. No hay mucha ciencia realmente, a lo mucho ajustar un modelo lineal para la columna de Turnos que muestra el programa para predecir en cuantos turnos podrá acabar la siguiente partida.</p>
<h3>CONCLUSIÓN</h3>
<p>Tras 6 meses de trabajo en este proyecto, concluimos que será necesario hacer más ensayos y jugar muchas más partidas para poder determinar una estrategia ganadora o por lo menos un conjunto de jugadas que sean más probables de conducir a una victoria, con posibilidad de extender el proyecto para incluso hacer sugerencias a un ratón estándo en una cierta posición incluyendo las casillas de los gatos o su posición actual.</p>
