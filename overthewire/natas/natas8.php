#!/usr/bin/php7.0

<?php
// undo encoding -> bin2hex(strrev(base64_encode($secret)))
$encodedSecret = '3d3d516343746d4d6d6c315669563362';

$secret = base64_decode(strrev(hex2bin($encodedSecret)));

echo($secret)

?>