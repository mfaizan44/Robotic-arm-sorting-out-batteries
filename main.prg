'Epson RC7 program to listed to command sent over TCP/IP network
'Valid commands are JUMP and GO, each command shall be followed by x, y, z, u

Global Integer x, y, z, u

Function main
	String indata$(0), receive$
	
	Motor On
	Power High
	Speed 20
	SpeedR 20
	Accel 20, 20
	SpeedS 20
	AccelS 20, 20
	
	Go Here :X(-182) :Y(500) :Z(400) :U(0) :V(0)

 ' use your robot actual IP address or 127.0.0.1 for simulator at local host
  SetNet #201, "127.0.0.1", 2001, CRLF
  
  OpenNet #201 As Server
  Print "Robot ready, listening to network"
  WaitNet #201
  OnErr GoTo ehandle

  Do
   Input #201, receive$
   ParseStr receive$, indata$(), " " ' convert to lower case later with LCase$
   Print "Received message: ", receive$
  
   ' if the command is jump x y z u
   If LCase$(indata$(0)) = "jump" Then
     	x = Val(Trim$(indata$(1)))
    	y = Val(Trim$(indata$(2)))
	    z = Val(indata$(3))
    	u = Val(indata$(4))
    	
   		Print "Jumping to x=", x, " y=", y, " z=", z, " u=", u
	   	Jump3 Here +Z(50), Here :X(0) :Y(y) :Z(z + 50), Here :X(x) :Y(y) :Z(z) :U(u)
	   	Print #201, "OK"
   EndIf
   
   ' if the command is go x y z
   If LCase$(indata$(0)) = "go" Then
     	x = Val(Trim$(indata$(1)))
    	y = Val(Trim$(indata$(2)))
	    z = Val(indata$(3))
    
   		Print "Going to x=", x, " y=", y, " z=", z, " u=", u
	   	Go Here :X(x) :Y(y) :Z(z)
 		 Print #201, "OK"
   EndIf
   
   ' if the command is pick
   If LCase$(indata$(0)) = "pick" Then
   		Print "Picking"
   		On 8
   		Print #201, "OK"
   EndIf
   
   ' if the command is drop
   If LCase$(indata$(0)) = "drop" Then
   		Print "Dropping"
     	Off 8
     	Print #201, "OK"
   EndIf
	
  Loop

  Exit Function

  ehandle:
	Call ErrFunc
    EResume Next
Fend
Function ErrFunc

  Print ErrMsg$(Err(0))
  Select Err(0)
   Case 2902
     OpenNet #201 As Server
     WaitNet #201

   Case 2910
     OpenNet #201 As Server

     WaitNet #201

   Default
     Error Err(0)

  Send
Fend


