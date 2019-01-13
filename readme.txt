■フレームセット
・フレームのサイズはパーセントでなく絶対値で設定する
絶対値でないとウィンドウサイズが変わるとレイアウトが崩れる


■掲示期限を過ぎた文書をゴミ箱に移す/削除する
1. 文書に掲示期限/削除フラグのフィールドを用意する
・掲示期限
本日より前の日付は指定できないようにする。
フィールド名：date_limit
フィールド種類：日付/時刻
入力の確認：
	diff_day := (date_limit - @Today) / 60 / 60 / 24;
	@If(
		diff_day < 0;
		@Prompt([OK]; "error"; "error");
		@Success
	)


・削除フラグ
種類は何でもよいが、テキストフィールドとして作成する。
ユーザが直接入力できないようにするため、段落非表示式を@Trueとして常に非表示としておく。
エージェントの実行により値を変更するため、編集可能としておく。
True でフラグオン、False でフラグオフを表す。
フィールド名：flag_delete
フィールド種類：テキスト
デフォルトの値："Flase"


2. エージェントにより削除フラグの値を変更
種類は式を選択。シンプルアクションでもフラグの変更は可能だが、
対象文書の選択に簡易検索しか使えないので、掲示期限を超過した文書の選択ができない。

ターゲットはDBの全文書にする。
Document Selection で対象文書を設定する。
上記の通り、簡易検索しか使えないため、この時点では単に削除フラグがオフの文書を選択する。
delete_flag に False が含まれる文書を選択するようにする。
(ここで文書選択を行わずに全文書選択とし、Actionでdelete_flagの値を見て判断してもいい)

Action でエージェントが実行する式を指定する。

	SELECT @All;
	diff_day := (@Today - @GetField("date_limit")) / 60 / 60 / 24;
	@If(
	    diff_day > 0;
	    @SetField("flag_delete"; "True");
	    ""
	)


3. ゴミ箱ビューを作成
・元のビュー
SELECT flag_delete="False"

・ゴミ箱ビュー
SELECT flag_delete="True"


4. ゴミ箱に移動した文書を元に戻せるようにする
flag_delete の Onchange イベントに以下のスクリプトを記述。
(Client、Lotusscript)
1でdate_limitの値は本日より前を指定できないので、
実際には最後のelseが実行された上で保存されることはない。


	Sub Onchange(Source As Field)	
		Dim uiws  As New NotesUIWorkspace
		Dim uidoc As NotesUIDocument
		Dim doc  As NotesDocument
		
		Set uidoc = uiws.CurrentDocument
		Set doc  = uidoc.Document
		
		Dim date_limit As Variant
		date_limit = doc.GetItemValue("date_limit")(0)
		
		Dim ndt_date_limit As NotesDateTime
		Set ndt_date_limit = New NotesDateTime(date_limit)
		
		Dim ndt_today As NotesDateTime
		Set ndt_today = New NotesDateTime(Today())
		
		Dim diff_sec As Double
		Dim diff_day As Double
		diff_sec = ndt_date_limit.TimeDifference(ndt_today)
		diff_day = diff_sec / 60 /60 /24
		
		If diff_day >= 0 Then
			Call uidoc.FieldSetText("flag_delete",  "False") 
		Else
			Call uidoc.FieldSetText("flag_delete",  "True") 
		End If
	End Sub


5. エージェントにより、ゴミ箱に移動されてからx日経過した文書を削除する
Document Selection で、delete_flag に True が含まれる文書を選択するようにする。

	SELECT @All;
	delete_day := 7;
	diff_day := (@Today - @GetField("date_limit")) / 60 / 60 / 24;
	@If(
		diff_day > delete_day;
		@DeleteDocument;
	    	""
	);
