#NoEnv
SendMode Input
SetWorkingDir %A_ScriptDir%

^q::
Send, {Enter}
Sleep, 1700
Send, ^b
Send, {Enter}
Send, crypto isakmp key
Send, {Esc}
Send, {Esc}
Loop, 3
{
Send, ^{Right}
}
Send, {Shift Down}
Loop, 15
{
Send, {Right}
}
Send {Shift Up}
Send, ^c
return
