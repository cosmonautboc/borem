Sub Click(Source As Navigator)
	' ��E�̒�`
	Dim posList List As Integer
	posList("���") = 0
	posList("AM_SE") = 1
	posList("M_CE") = 2
	posList("SM") = 3
	posList("����") = 4
	posList("���̑�") = 5
	
     ' ����̒�`
	Dim deptList List As Integer
	deptList("�Z�p�{��") = 0
	deptList("�c�Ɩ{��") = 1
	deptList("�v��{��") = 2
	deptList("���̑�") = 3
	
	' ���[�U�̖�E���擾���ĕϊ�
	' �ϊ���� posList �̃^�O���ɍ��킹�邱��
	userPos = "AM��s"
	If userPos = "AM" Or userPos = "SE" Or userPos = "AM��s" Then
		userPos = "AM_SE"
	Elseif userPos = "M" Or userPos = "CE" Or userPos = "M��s" Then
		userPos = "M_CE"
	Else
		userPos = "���̑�"
	End If
	' �S�p���p���܂߂� �����������
	
	' ���[�U�̏���������擾���ĕϊ�
	' �ϊ���� deptList �̃^�O���ɍ��킹�邱��
	userDept = "��P�J����"
	If userDept = "��P�J����" Or userDept = "��Q�J����" Then
		userDept = "�J���{��"
	Elseif userDept = "��P�c�ƕ�" Or userDept = "��Q�c�ƕ�" Then
		userPos = "�c�Ɩ{��"
	Else
		userPos = "���̑�"
	End If
	
	' �A�N�Z�X����e�[�u�����쐬
	' 1�Ԗڂ̗v�f���� posList �A2�Ԗڂ̗v�f���� deptList �A���ꂼ��̗v�f���ɍ��킹�邱��
	' LotusScript�ł͋L�q�����v�f��+1�̗v�f�����z�񂪍쐬�����_�ɒ���
	' tmp(5) �Ƃ����ꍇ�ɂ� tmp(0)�`tmp(5) �܂�6�̗v�f������
	' ���̂��� postList �� deptList �̍ő�l���w�肷��΂悢
	Dim acTable(5, 3) As Boolean
	
	' �L�ژR��h�~�̂��� False �o������
	Forall ac In acTable
		ac = False
	End Forall
	
	' True:�A�N�Z�X�\  False:�A�N�Z�X�s��
	acTable("���", "�Z�p�{��") = True
	acTable("AM_SE", "�Z�p�{��") = True
	acTable("M_CE", "�Z�p�{��") = True
	acTable("SM", "�Z�p�{��") = True
	acTable("SM", "�Z�p�{��") = True
	
	' ���̐�Ɍʂ̃A�N�Z�X���������
	' �����́��ł͓��ꂸ�A���̐�Œ�`
	
End Sub