■コンソール画面とラズパイマークの変更
http://steeledge2.blogspot.com/2019/05/linuxraspberrypi.html
https://bitset.jp/blog/raspi_plymouth

■虹色画面の変更
https://teratail.com/questions/185282
https://www.raspberrypi.org/forums/viewtopic.php?t=17449
https://www.raspberrypi.org/forums/viewtopic.php?t=235228
https://www.raspberrypi.org/forums/viewtopic.php?t=189666
https://raspberrypi.stackexchange.com/questions/22047/disabling-rainbow-splash-screen-does-not-work
https://scribles.net/silent-boot-up-on-raspbian-stretch/
https://scribles.net/lightning-bolt-under-voltage-warning-on-raspberry-pi/
https://scribles.net/customizing-boot-up-screen-on-raspberry-pi/

基本的には一番下のリンクに従えばよい。

■メニューバーを消す
バーを右クリック → パネルの設定 → 高度な設定 → 使わないときはパネルを最小化する にチェック、最小化時のサイズ を0にする 0にしてもカーソルを上端に持っていくと表示される
このやり方だと起動時にカーソルが上端にあるので表示されてしまう
メニューバーの位置を下に持ってきても、カーソルの初期位置がメニューバーになるようでこちらも表示されてしまう

https://unix.stackexchange.com/questions/462458/how-do-i-disable-the-taskbar-menubar-in-lxde-on-raspbian-stretch
このやり方だと完全にメニューバーが消えるがGUIでアプリなどを起動できない
windowsキーを押してもメニューが出てこない
運用時ならいいが、開発時は面倒
デスクトップに空のフォルダを用意して、そこを右クリックしてターミナルを開く方法もある
アイコンの文字と画像を黒にする必要がある


■ゴミ箱を消す
ゴミ箱を右クリック → デスクトップから除去

■デスクトップを黒一色に変更、デスクトップに何も表示しない
デスクトップを右クリック → デスクトップの設定 → Desktop タブの Layout を No image に、Color を黒にする
Desktop タブ下部の Documents Wastebasket Mounted Disks のチェックをすべて外す
Wastebasket はゴミ箱のこと

■カーソルを消す
https://blog.withachristianwife.com/2017/04/09/disable-mouse-cursor-in-raspberry-pi/
時間を0にすると常時非表示になる？ならない

■起動高速化
https://nw-electric.way-nifty.com/blog/2017/04/raspberry-pi-ze.html






■やりたいこと
・DBのあるビューの全文書に含まれる添付ファイルをダウンロード
・保存先を指定
・タイトルをフォルダ名にしてフォルダを自動作成する
・同名のフォルダやファイルがあれば自動的に別名保存


■添付ファイルをディスクに保存する
https://guylocke.blogspot.com/2008/06/blog-post_18.html

■データベース中の全文書を取得する
https://guylocke.blogspot.com/2008/05/blog-post_07.html

■ビューの文書を順番にすべて取得する
https://www.xpages.jp/XSnippetsJ.nsf/snippet.xsp?id=%E3%83%92%E3%82%99%E3%83%A5%E3%83%BC%E3%81%AE%E6%96%87%E6%9B%B8%E3%82%92%E9%A0%86%E7%95%AA%E3%81%AB%E3%81%99%E3%81%B8%E3%82%99%E3%81%A6%E5%8F%96%E5%BE%97%E3%81%99%E3%82%8B%28notesview-%E3%82%AF%E3%83%A9%E3%82%B9getfirstdocument-getnextdocument-%E3%83%A1%E3%82%BD%E3%83%83%E3%83%88%E3%82%99%29
https://help.hcltechsw.com/dom_designer/10.0.1/basic/H_CURRENTVIEW_PROPERTY_1026_ABOUT.html
https://help.hcltechsw.com/dom_designer/9.0.1/appdev/H_EXAMPLES_VIEW_PROPERTY.html

■文書の全アイテムにアクセス
https://help.hcltechsw.com/dom_designer/9.0.1/appdev/H_EXAMPLES_ITEMS_PROPERTY.html

■ファイル/フォルダ有無を確認する
https://zaq123edc.hateblo.jp/entry/2013/06/28/132447
https://help.hcltechsw.com/dom_designer/10.0.1/basic/LSAZ_DIR_FUNCTION.html
ファイル有無はDIRを使ってフォルダ内にファイルがあるか否かを判定すればよい
フォルダ有無は、そのフォルダの上位フォルダの中でDIRを使って判定する必要があるか？

■フォルダを作成する
https://guylocke.blogspot.com/2008/06/blog-post_05.html
https://help.hcltechsw.com/dom_designer/10.0.1/basic/LSAZ_MKDIR_STATEMENT_EX.html

■フォルダを指定する
https://help.hcltechsw.com/dom_designer/10.0.1/basic/H_SAVEFILEDIALOG_METHOD_7107_ABOUT.html

■script
Dim ws As New NotesUIWorkspace

' 保存先を指定
folder = ws.SaveFileDialog(True, "保存先を指定")
If Not(Isempty(folder)) Then
    
    ' 現在のビューを取得
    Dim uiws As New NotesUIWorkspace
    Dim uiview As NotesUIView
    Dim view As NotesView
    Set uiview = uiws.CurrentView
    Set view = uiview.View
    
    ' ビュー中の全文書を順番に取得する
    Dim doc As NotesDocument
    Set doc = view.GetFirstDocument
    While Not(doc Is Nothing)
        ' 文書にオブジェクトまたは添付ファイルがあるか否か判定
        If doc.HasEmbedded then
            Dim flag_mkdir As Boolean
            flag_mkdir = False
            
            ' 文書の全フィールドを取得
            Forall item In doc.Items 
                ' フィールドがリッチテキストか否か判定
                If item.Type = RICHTEXT Then
                    ' リッチテキストの全オブジェクトと添付ファイルを取得
                    Forall obj In item.EmbeddedObjects
                        ' 添付ファイルか否か判断(OLEオブジェクトとは扱いが異なるため)
                        If obj.Type = EMBED_ATTACHMENT Then
                            ' フォルダ未作成の場合にはフォルダを新規作成する
                            If Not(flag_mkdir) Then
                                ' [未実装]同名のフォルダがないか確認
                                
                                ' パスの区切り(\)が必要？
                                Mkdir folder & doc.Title(0)
                            End If
                            
                            ' [未実装]同名のファイルがないか確認
                            
                            ' 添付ファイルを保存
                            Call obj.ExtractFile(folder & doc.Title(0) & obj.Name)
                        End If
                    End Forall
                End If
            End Forall
        End If
        
        ' 次の文書を取得
        Set doc = view.GetNextDocument(doc)
   Wend 
End If

