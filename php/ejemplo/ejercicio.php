<?php
function area_triangulo(){
    $base_longitud = 12;
    $altura_longitud = 25;
    $Area = $base_longitud * $altura_longitud / 2;
    echo "el area del tringualo es: $Area " ."\n";
}

area_triangulo();



function calculadora_de_propinas($factura,$propina,$personas){
    $calculo = $factura * $propina / 100;
    $pago_total = ($factura + $propina) / $personas;
    echo "el pago total que deb hacer cada persona es $pago_total" ."\n";
}

calculadora_de_propinas(120.000,20.000,3);



function condiciones($numero){
    if ($numero > 30 ){
        echo "el numero es mayor a 30";
    }elseif ($numero >= 20){
        echo "el numero es  mayor a 20 o es 20";
    }elseif($numero > 10){
        echo "el numero es mayor a 10";
    }elseif ($numero < 0){
        echo "el numero es un entero negativo"."\n";
    }else{
        echo "el numero es menor o igual a 10";
    }
} 


condiciones(-12);



// para poder recorrer en un bucle foreach una cadena de texto tienes que convertila en numero y es co esta funcion str_split($la_variable que quieres rrecorrer)
function  listas(){
    $lista = [];
    $texto = [1,2,3,4,5,3,4,5,6] ;
    foreach ($texto as $text){
        if ($text >= 10) {
            array_push($lista,1);
        }elseif($text > 5 ){
            array_push($lista,2);
        }else{
            array_push($lista,3);
        }    
    }
    print_r($lista);
    print_r($texto);
}

listas();


$emplado_datos = array("nombre" => "santiago","edad" => 23 , "salario" => 2.500, "cargo" => "desarrollador sotfware");
$emplado_datos1 = array("nombre" => "sebastian","edad" => 22 , "salario" => 1.330, "cargo" => "desarrollador sotfware");
$emplado_datos2 = array("nombre" => "andres","edad" => 25 , "salario" => 4.799, "cargo" => "desarrollador sotfware");
$emplado_datos3 = array("nombre" => "pablo","edad" => 18 , "salario" => 2.000, "cargo" => "desarrollador sotfware");
$emplado_datos4 = array("nombre" => "juan","edad" => 32 , "salario" => 22.300, "cargo" => "senior desarrollador sotfware");
print_r($emplado_datos) . "\n";

$edades = array();

// Recorre cada diccionario en el array
foreach ($emplado_datos as $persona) {
    // Verifica si la clave "edad" existe en el diccionario
    if (isset($persona["edad"])) {
        // Agrega la edad al array de edades
        $edades[] = $persona["edad"];
    }
}

// Ahora $edades contiene todas las edades
print_r($edades);




function sombrero_aleatorio($pregunta1){
    //creamos listas vacias
    $Gryffindor = [];
    $Slytherin = [];
    $Hufflepuff = [];
    $Ravenclaw = [];

    $pregunta1 = $pregunta1;
    if ($pregunra1 == "a"){
        array_push($Gryffindor,10);
    }elseif($preguta1 =="b"){
        array_push($Slytherin,10);
    }elseif($pregunta1 == "c"){
        array_push($Hufflepuff,10);
    }else{
        array_push($Ravenclaw,10);
    }

    $suma = $Gryffindor + $Hufflepuff + $Slytherin + $Ravenclaw;

    
 
 
  

}



?>