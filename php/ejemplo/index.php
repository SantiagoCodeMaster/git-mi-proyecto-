<?php 
//hola 
echo "hola mundo\n";
/*  
comenaterio largo
muy largo
*/
$my_string = "esto es una cadena de texto";
echo $my_string . "\n";
$my_string = "aqui cambia el valor del la variable". "\n";
echo $my_string;
echo gettype($my_string). "\n";

$my_string = 6;//tipado dinamico
echo $my_string . "\n";

// datos numeroicos enteros y decimales
$my_int = 67;
$my_int = $my_int + 4;
echo $my_int . "\n";
echo $my_int - 6 . "\n";


$my_double = 6.7;
echo gettype($my_double). "\n"; 
$my_double = $my_double + $my_int  ."\n";
echo $my_double;


//buelano 
$my_bool = true;
echo $my_bool . "\n";
$my_bool = false;
echo $my_bool= 0 . "\n";
echo gettype($my_bool) . "\n";

echo "el valor de mi entero es $my_int   y el de my bool es $my_bool ";

//constantes

const MY_CONSTANT = "valor de la constante". "\n";
echo MY_CONSTANT; 


//listas 

$my_array = [$my_string,$my_int,$my_double];

echo  gettype($my_array) . "\n";

echo $my_array[0]. "\n";
echo $my_array[1]. "\n";
echo $my_array[2]. "\n";

array_push($my_array,$my_bool); //es como decir append 
print_r($my_array) . "\n";


//diccionario

$my_dict = array("string" => $my_string,"int" => $my_int,"double" => $my_double,"bool" => $my_bool); 
echo gettype($my_dict). "\n";
print_r($my_dict). "\n";
echo $my_dict["int"] . "\n";


//set / conjunto

array_push($my_array,"Brais");
array_push($my_array,"Brais");
print_r($my_array);

print_r(array_unique($my_array));

//flujo de datos 

for ($index = 0; $index < 10; $index ++){
    echo $index . "\n";
}

foreach ($my_array as $my_item) {
    echo $my_item . "\n";
}
 
$index = 0;
while($index < sizeof($my_array)-1){
  echo $my_array[$index]. "\n";
  $index++;
}

$my_int = 14;

if ($my_int == 11){
  echo "el valor es 11" . "\n";
} elseif ($my_int == 12){
  echo "el valor es 12" . "\n";
}else {
  echo "el valor no es ni 11 ni 12 es $my_int" ."\n";
}


$it = 154;
$int = 120;

if ($int == 120 && $it == 154){
  echo "el primer numero  es $it y el segundo es $int". "\n";
}elseif($int == 12 && $it == 134){
  echo "muy bien";
}else {
 echo "muy mal";
}

//funciones

function print_number(){
  echo 12 . "\n";
}

$numero = print_number();
echo $numero;

function codigo_konami($konami){
  if ($konami == "arriba,arriba,abajo,abajo,izquierda,derecha,izquierda,derecha,B,A"){
    echo "codigo konami activado" ."\n";
  }else{
    echo "codigo incorrecto" . "\n";
  }
  
} 
codigo_konami("arriba,arriba,abajo,abajo,izquierda,derecha,izquierda,derecha,B,A");



//POO  
class MyClass {
  public $name;
  public $age;

  function __construct($name,$age){
    $this -> name = $name;
    $this -> age = $age;

  }

}

$my_class = new MyClass("santiago",23);
print_r($my_class);
echo $my_class -> name. "\n";




?>

