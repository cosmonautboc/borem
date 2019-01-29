Sub Click(Source As Navigator)
	' 役職の定義
	Dim posList List As Integer
	posList("一般") = 0
	posList("AM_SE") = 1
	posList("M_CE") = 2
	posList("SM") = 3
	posList("役員") = 4
	posList("その他") = 5
	
     ' 部門の定義
	Dim deptList List As Integer
	deptList("技術本部") = 0
	deptList("営業本部") = 1
	deptList("計器本部") = 2
	deptList("その他") = 3
	
	' ユーザの役職を取得して変換
	' 変換先は posList のタグ名に合わせること
	userPos = "AM代行"
	If userPos = "AM" Or userPos = "SE" Or userPos = "AM代行" Then
		userPos = "AM_SE"
	Elseif userPos = "M" Or userPos = "CE" Or userPos = "M代行" Then
		userPos = "M_CE"
	Else
		userPos = "その他"
	End If
	' 全角半角も含める 役員も入れる
	
	' ユーザの所属部門を取得して変換
	' 変換先は deptList のタグ名に合わせること
	userDept = "第１開発部"
	If userDept = "第１開発部" Or userDept = "第２開発部" Then
		userDept = "開発本部"
	Elseif userDept = "第１営業部" Or userDept = "第２営業部" Then
		userPos = "営業本部"
	Else
		userPos = "その他"
	End If
	
	' アクセス制御テーブルを作成
	' 1番目の要素数は posList 、2番目の要素数は deptList 、それぞれの要素数に合わせること
	' LotusScriptでは記述した要素数+1つの要素を持つ配列が作成される点に注意
	' tmp(5) とした場合には tmp(0)～tmp(5) まで6つの要素を持つ
	' そのため postList と deptList の最大値を指定すればよい
	Dim acTable(5, 3) As Boolean
	
	' 記載漏れ防止のため False 出初期化
	Forall ac In acTable
		ac = False
	End Forall
	
	' True:アクセス可能  False:アクセス不可
	acTable("一般", "技術本部") = True
	acTable("AM_SE", "技術本部") = True
	acTable("M_CE", "技術本部") = True
	acTable("SM", "技術本部") = True
	acTable("SM", "技術本部") = True
	
	' この先に個別のアクセス制御を入れる
	' 役員は↑では入れず、この先で定義
	
End Sub