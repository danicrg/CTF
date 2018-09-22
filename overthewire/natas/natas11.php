<?php

$defaultdata = array( "showpassword"=>"no", "bgcolor"=>"#ffffff");

$cookie_data = 'ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSEV4sFxFeaAw%3D';

$xor_encrypted = base64_decode($cookie_data);
$xor_inData = json_encode($defaultdata);


$key = '';
for($i=0;$i<strlen($xor_encrypted);$i++) {
    $key .= $xor_encrypted[$i] ^ $xor_inData[$i];
    }

function xor_encrypt($in) {
    $key = 'qw8J';
    $text = $in;
    $outText = '';

    // Iterate through each character
    for($i=0;$i<strlen($text);$i++) {
    $outText .= $text[$i] ^ $key[$i % strlen($key)];
    }

    return $outText;
}

$data = array( "showpassword"=>"yes", "bgcolor"=>"#ffffff");

echo(base64_encode(xor_encrypt(json_encode($data))));





?>