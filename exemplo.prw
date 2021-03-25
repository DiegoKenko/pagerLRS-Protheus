USER Function ChamaPag(nOpcP)

	Local cNPAger	:= cValToChar(SZV->ZV_PAGER)
	Local cExe	:= 'pager.exe'
	Local cUser 	:= ''
	Local cDominio	:= ''
	Local cCamDes  := "C:\Pager\pager\"
	Private oFile 	:= FWFileReader():New(cCamDes + cNPAger + '.txt')
	Private lChamou := .F.

	// Validações a serem feitas
	IF EMPTY(SZV->ZV_PAGER) // Não existe pager atribuido
		MsgInfo("Não há pager atribuído para esse movimento","")
		Return
	EndIf

	FErase(cCamDes + cNPAger + '.txt')

	ShellExecute("open",cCamDes + cExe,cNPAger + ' ' + cValToChar(nOpcP),cCamDes,0)

	MsAguarde({|| ExePAger()},"Chamando pager","Aguarde...")


return lChamou