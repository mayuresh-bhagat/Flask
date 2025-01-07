<?php
session_start();
ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
error_reporting(E_ALL);
include('include/connection.php');
include('include/sweetalert.php');

// Check if the form is submitted
if (isset($_POST['submit'])) {
    // Retrieve and sanitize inputs
    $name = $_POST['name'];
    $mobile_no = $_POST['mobile_no'];
    $gotra = $_POST['gotra'];
    $email = $_POST['email'];
    $rakkam = $_POST['rakkam'];
    $saman = $_POST['saman'];
    $praman = $_POST['praman'];
    $by_user = $_POST['by_user'];
    $status = $_POST['status'];

    // Check if mobile number already exists
    $check_mobile_query = "SELECT * FROM puja_saman WHERE mobile_no = ?";
    $stmt = $conn->prepare($check_mobile_query);
    $stmt->bind_param("s", $mobile_no);
    $stmt->execute();
    $result = $stmt->get_result();

    if ($result->num_rows > 0) {
        echo "<script>
                alert('This mobile number is already used, please enter a different number.');
                window.location.href = 'puja_saman_db.php';
              </script>";
        exit();
    }
    $stmt->close();

    // Insert the record using a prepared statement
    $sql = "INSERT INTO puja_saman (name, mobile_no, gotra, email, rakkam, saman, praman, by_user, status) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)";
    $stmt = $conn->prepare($sql);
    $stmt->bind_param(
        "ssssiiiss",
        $name,
        $mobile_no,
        $gotra,
        $email,
        $rakkam,
        $saman,
        $praman,
        $by_user,
        $status
    );

    if ($stmt->execute()) {
        echo "<script>
                alert('Record saved successfully!');
                window.location.href = 'puja_saman_db.php';
              </script>";
    } else {
        echo "<script>
                alert('Error saving the record: " . $stmt->error . "');
                window.location.href = 'puja_saman_db.php';
              </script>";
    }

    $stmt->close();
}

$conn->close();
?>
