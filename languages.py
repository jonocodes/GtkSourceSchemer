#!/usr/bin/python

# please keep these in alphabetical order so it is easy to follow
# see available languages: /usr/share/gtksourceview-3.0/language-specs

samples = {}

samples['ada'] = """
with Ada.Text_Io; use Ada.Text_Io;
 
 procedure Doors is
    type Door_State is (Closed, Open);
    type Door_List is array(Positive range 1..100) of Door_State;
    The_Doors : Door_List := (others => Closed);
 begin
    for I in 1..100 loop
       for J in The_Doors'range loop
          if J mod I = 0 then
             if The_Doors(J) = Closed then
                 The_Doors(J) := Open;
             else
                The_Doors(J) := Closed;
             end if;
          end if;
       end loop;
    end loop;
    for I in The_Doors'range loop
       Put_Line(Integer'Image(I) & " is " & Door_State'Image(The_Doors(I)));
    end loop;
 end Doors;
"""

samples['asp'] = """
<html>
<body>
<form action="demo_reqquery.asp" method="get">
Your name: <input type="text" name="fname" size="20" />
<input type="submit" value="Submit" />
</form>
<%
dim fname
fname=Request.QueryString("fname")
If fname<>"" Then
      Response.Write("Hello " & fname & "!<br />")
      Response.Write("How are you today?")
End If
%>
</body>
</html>
"""

samples['awk'] = """
BEGIN {
  for(i=1; i <= 100; i++) {
    doors[i] = 0 # close the doors
  }
  for(i=1; i <= 100; i++) {
    if ( int(sqrt(i)) == sqrt(i) ) {
      doors[i] = 1
    }
  }
  for(i=1; i <= 100; i++)
  {
    print i, doors[i] ? "open" : "close"
  }
}
"""

# do not remove this language
samples['c'] = """
/* Some comments */
#include <stdio.h>
 
int main()
{
  int square = 1, increment = 3, door;
  for (door = 1; door <= 100; ++door)
  {
    printf("door #%d", door);
    if (door == square)
    {
      printf(" is open.");
      square += increment;
      increment += 2;
    }
    else
      printf(" is closed.");
  }
  return 0;
}
"""

samples['c-sharp'] ="""
// Creates and initializes a new integer Array
int[] intArray = new int[5] { 1, 2, 3, 4, 5 };
//same as
int[] intArray = new int[]{ 1, 2, 3, 4, 5 };
//same as
int[] intArray = { 1, 2, 3, 4, 5 };
 
//Arrays are zero-based
string[] stringArr = new string[5];
stringArr[0] = "string";
"""

samples['diff'] = """
--- xinetd.d/tftp       2003-12-17 13:11:20.000000000 -0500
+++ ./tftp      2004-01-22 11:46:14.479497688 -0500
@@ -10,7 +10,7 @@
        wait                    = yes
        user                    = root
        server                  = /usr/sbin/in.tftpd
-       server_args             = -s /tftpboot
+       server_args             = -p -u tftpd -s /tftpboot
        disable                 = yes
        per_source              = 11
        cps                     = 100 2
"""

samples['php'] = """
/* ygtyuy */
print 'hello world';
"""

