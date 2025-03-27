<!DOCTYPE html>
<html>
<head>
    <title>Second Form</title>
</head>
<body>

    <table align="center" border="0" cellpadding="10" cellspacing="0">
        <tr>
            <th colspan="2">
                <h2>Form 2: Display Data</h2>
            </th>
        </tr>
        <?php
            // Securely retrieve data from form1.php (via POST)
            if ($_SERVER["REQUEST_METHOD"] == "POST" && isset($_POST['name']) && isset($_POST['email'])) {
                // Using htmlspecialchars to prevent XSS
                $name = htmlspecialchars($_POST['name']);
                $email = htmlspecialchars($_POST['email']);
            } else {
                $name = $email = '';
            }
        ?>
        <tr>
            <td>Name:</td>
            <td><?php echo $name; ?></td>
        </tr>
        <tr>
            <td>Email:</td>
            <td><?php echo $email; ?></td>
        </tr>

        <tr>
            <th colspan="2">
                <h3>Modify Details:</h3>
            </th>
        </tr>
        <form action="form2.php" method="POST">
            <tr>
                <td><label for="name">Name:</label></td>
                <td><input type="text" id="name" name="name" value="<?php echo $name; ?>" required></td>
            </tr>
            <tr>
                <td><label for="email">Email:</label></td>
                <td><input type="email" id="email" name="email" value="<?php echo $email; ?>" required></td>
            </tr>
            <tr>
                <td colspan="2" align="center">
                    <input type="submit" value="Update">
                </td>
            </tr>
        </form>
    </table>

</body>
</html>
