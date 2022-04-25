<?php
/**
 * @file table.php
 */

/**
 * @brief Displays a table header
 * @param $columns Array of table headings
 */
function PrintTableHeader( $columns )
{
   $bgColor = "#b4cdcd"; // LightCyan3
   $fgColor = "#ffffff"; // White

   printf( "<table
               border='1'
               cellpadding='5'
               cellspacing='0'>\n" );

   printf( "<tr bgcolor='%s'
                style='color: %s'>\n",
                   $bgColor,
                   $fgColor );

   foreach ( $columns as $name )
      printf( "<th> %s </th>\n", $name );

   printf( "</tr>\n" );

}  // function PrintTableHeader();


/**
 * @brief Displays a table row
 * @param $id ID of the row
 * @param $row Hash table cells
 */
function PrintTableRow( $id, $row )
{
   static $rowCount = 0;
   $fgColor = "#000000"; // Black

   if ( $rowCount % 2 )  // not even
      $bgColor = "#d1eeee"; // LtCyan2
   else
      $bgColor = "#e0ffff"; // LtCyan

   printf( "<tr valign='top'
                bgcolor='%s'
                style='color: %s'>\n",
                   $bgColor,
                   $fgColor );

   foreach ( $row as $key => $value )
   {
      if ( $key == 'title' )
      {
         $file = "create.php";
         $title = $row[$key];

         $cell = sprintf( "<a href='%s?id=%d'>%s</a>",
                             $file, $id, $title );
      }
      else
      {
         $cell = $row[$key];
      }

      printf( "<td> %s </td>\n", $cell );
   }

   printf( "<td>  <!-- Action -->
               <input
                  type='button'
                  name='delete'
                  value='Delete?'
                  onClick=\"confirmDelete( %d,
                                           '%s' );\" />
            </td>\n", $id, $title );

   printf( "</tr>\n" );

   // prep for next function call
   $rowCount++;

}  // function PrintTableRow();
?>