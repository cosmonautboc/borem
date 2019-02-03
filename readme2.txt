%REM
	Agent KeepPrivateCtrl
	Created Feb 3, 2019 by John Doe/John Doe
	Description: Comments for Agent
%END REM
Option Public
Option Declare


Sub Initialize
	Dim uiwp As New NotesUIWorkspace
	Dim retPassPrompt As Variant
	retPassPrompt = uiwp.Prompt(PROMPT_PASSWORD, "pass", "pass")

	If retPassPrompt = "dev38" Then
		
		Dim choiceList(3) As String
		choiceList(0) = "1:check value"
		choiceList(1) = "2:delete value"
		choiceList(2) = "3:replace value to 0"
		choiceList(3) = "4:replace value to 1"

		Dim retListPrompt As Variant		
		retListPrompt = uiwp.Prompt(PROMPT_OKCANCELLIST, "choice", "choice", choiceList(0), choiceList)

		Dim session As New NotesSession
		Dim db As NotesDatabase
		Dim docs As NotesDocumentCollection
		Dim doc As NotesDocument
		
		'�J�����g�f�[�^�x�[�X��ݒ肷��
		Set db = session.CurrentDatabase
		
		'�r���[����I�����ꂽ�������擾����
		Set docs = db.UnprocessedDocuments

		'�S���������̌J��Ԃ�
		Dim i As Long
		For i = 1 To docs.Count
			'GetNthDocument( i )�́Ai�Ԗڂ̕������擾����Ƃ����Ӗ�
			'���̂Ƃ��̕����̕��т̓f�[�^�x�[�X�ɕۑ����ꂽ��
			Set doc = docs.GetNthDocument( i )
			
			If retListPrompt = "1:check value" Then
				Dim title As Variant
				Dim keepPrivate As Variant
				title = doc.Getitemvalue("title")
				keepPrivate = doc.Getitemvalue("$KeepPrivate")
				MessageBox "title:" + title(0) + Chr$(13) + "hasItem:" + CStr(doc.Hasitem("$KeepPrivate")) + Chr$(13) +"$KeepPrivate:" + keepPrivate(0)

			ElseIf retListPrompt = "2:delete value" Then
				Call doc.Removeitem("$KeepPrivate")
				Call doc.Save(False, False)

			ElseIf retListPrompt = "3:replace value to 0" Then
				Call doc.ReplaceItemValue("$KeepPrivate", "0")
				Call doc.Save(False, False)

			ElseIf retListPrompt = "4:replace value to 1" Then
				Call doc.ReplaceItemValue("$KeepPrivate", "1")
				Call doc.Save(False, False)

			End If
		Next
	End If
End Sub