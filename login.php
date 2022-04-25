<?php
   /**
    * @file login.php
    */
   $host = "localhost";
   $username = "root";
   $password = "";
   $dbName = "cookbookdb";

   // 1. & 2. Connect and use the database
   $conn = mysqli_connect( $host,
                           $username,
                           $password,
                           $dbName );

   if ( mysqli_connect_errno() )  // not connected
   {
      die( "Could not connect $host to
            database.<br />" .
            mysqli_error( $conn ) );
   }
?>