var tipuesearch = {"pages":[{"title":"About","text":"Pyslvs.com 網誌 假如您要連結到先前的網站內容, 請至 https://kmolyuan.github.io/pyslvs/ , 目前的 http://pyslvs.com 網站倉儲內容位於 https://github.com/pyslvs/pyslvs.github.io . Pyslvs 是一套以 Python3 及 PyQt5 打造的平面機構模擬與合成套件.","tags":"misc","url":"./pages/about/"},{"title":"Flow chart of Pyslvs synthesis function","text":"Flow chart of Pyslvs synthesis function Number and type synthesis Dimensional synthesis","tags":"開發","url":"./yuan_2018-03-26.html"},{"title":"Pyslvs v18.3.0 - 02/28","text":"Auto configuration algorithm 自動配置演算法 Auto configuration algorithm 自動配置演算法 A function that can auto configure the solutions. 一個可以自動配置解決方案的功能。","tags":"開發","url":"./yuan_2018-02-28.html"},{"title":"Pyslvs v18.2.0 - 02/22","text":"Update information 更新資訊 Update information 更新資訊 Update information about dimensional synthesis function. 尺寸合成功能的更新資訊。","tags":"開發","url":"./yuan_2018-02-22.html"},{"title":"Pyslvs v18.2.0 - 02/11","text":"Ball lifter mechanism synthesis test 提球機構合成測試 Ball lifter mechanism synthesis test 提球機構合成測試 The new synthesis options will support algorithms that end with fitness, and we will conduct small calculations for ball lifter mechanisms with two target paths. 新的合成設定中將支援隨適應值結束演算法，針對有兩個目標路徑的提球機構展開小型演算測試。 The construction of the ball lifter mechanism is so variable that it takes 6 minutes to 20 minutes to calculate the fitness below 100. 提球機構的變數較多，導致演算適應值至 100 以下的所需時間為 6 分鐘到 20 分鐘不等。 In addition, the staggered position of two target paths will also affect the result. 另外，兩段目標路徑的交錯位置也會影結果。","tags":"開發","url":"./yuan_2018-02-11.html"},{"title":"Pyslvs v18.1.0 - 01/25","text":"Triangular iteration 三角迭代展示影片 Triangular iteration demo video 三角迭代展示影片 Video - English version: Video - Traditional Chinese version: Triangular iteration function will be update in version 18.1. But the profile can not apply in dimensional synthesis function currently. 三角迭代功能將會於 18.1 版更新。 但是目前的配置資訊不能應用於尺寸合成功能。","tags":"開發","url":"./yuan_2018-01-25.html"},{"title":"Pyslvs v18.1.0 - 01/07","text":"Topological library 拓樸程式庫 Atlas function 圖譜功能 Topological library 拓樸程式庫 For better computing performance, the number synthesis library changed to Cython prepared. Which extracted some of the functions of NetworkX module, translated into Cython syntax. 為取得更好的運算效能，數目合成的程式庫改為 Cython 編寫。其中提取 NetworkX 模組的部份功能，轉譯為 Cython 語法。 Graph class edges public object ( tuple ) nodes public object ( tuple ) adj public object ( dict ) neighbors cpp function has_triangles cpp function is_connected cpp function degree cpp function number_of_edges cpp function __len__ cpp function GraphMatcher class G1 public Graph G2 public Graph G1_nodes object ( set ) G2_nodes object ( set ) mapping object ( set ) core_1 public object ( set ) core_2 public object ( set ) inout_1 public object ( set ) inout_2 public object ( set ) state GMState initialize c function candidate_pairs_iter python generator is_isomorphic cpp function isomorphisms_iter python generator match python generator semantic_feasibility c function syntactic_feasibility c function GMState class GM GraphMatcher G1_node object ( None or int ) G2_node object ( None or int ) depth int Atlas function 圖譜功能 Use the text file to store the atlas, the expression is the edge attribute in Graph class. You can also load text files into Pyslvs for processing. 使用文字文件儲存圖譜，表示式為 Graph 類型的 edges 屬性。 另外還可以將文字文件載入 Pyslvs 中處理。","tags":"開發","url":"./yuan_2018-01-07.html"},{"title":"Pyslvs 2018 Plan","text":"About release 關於發佈 About release 關於發佈 Since 2018, Pyslvs will take the monthly release of the version update. The format of the version will be numbered as {year}.{month}.{patch} . The progress of the update will be updated in both English and Traditional Chinese in this blog. The \"開發\" category in this blog will refer to questions (concepts) that Pyslvs faces and how to use the existing knowledge collation to reach a solution to the problem. 自 2018 年開始，Pyslvs 將會採取每月釋出的方式進行版本更新。版本格式將以 {year}.{month}.{patch} 的方式編號。 更新進度將以英文與繁體中文的方式全部更新在本網誌。 本網誌的「開發」類別中將會提及 Pyslvs 面臨的問題（概念），並如何使用現有的知識歸類，達成問題的解決途徑。","tags":"開發","url":"./yuan_2018_plan.html"},{"title":"Pyslvs v0.9 - 12/12","text":"Graphviz 引擎限制（已解決） Beta 3 Release Graphviz 引擎限制（已解決） 最後使用 NetworkX 呼叫 Pydot 模組克服障礙。 Pydot 模組的原理是使用 command line 擷取回傳資訊，因此只要系統可以呼叫「dot」等指令即可。 即使不安裝 Graphviz，Pyslvs 只會跳出提醒視窗，可以選擇 Network 的引擎，或是馬上安裝，不用重開 Pyslvs 也可以重繪圖譜。 嘗試之餘也完成了轉換式，可以接頭表示；另外還有排除退化結果的功能。 Beta 3 Release 先釋出測試版，包含 beta 2 之後的進度。 舊的函式錯誤修復。 PMKS 表示式的 P 和 RP 接頭已經支援。 矩形選取模式。 類型合成圖譜。 更多範例。","tags":"開發","url":"./yuan_2017-12-12.html"},{"title":"Pyslvs v0.9 - 12/10","text":"QIcon 透明背景繪製 Graphviz 引擎限制 QIcon 透明背景繪製 使用 QImage 取代 QPixmap 可以繪製出具有透明背景的圖示或影像。 image = QImage(QSize(*rect), QImage.Format_ARGB32_Premultiplied) image.fill(Qt.transparent) painter = QPainter(image) painter.translate(image.width()/2, image.height()/2) painter.end() return QIcon(QPixmap.fromImage(image).scaledToWidth(width)) 從 QIcon 轉為 QPixmap 可以用 pixmap(size: QSize) 或 pixmap(w: float, h: float) 方法。 listWidget.currentItem().icon().pixmap(listWidget.iconSize()) Graphviz 引擎限制 NetworkX 透過 PyGraphviz 引入 Graphviz 的繪圖演算法，提供更好的節點位置在圖譜中表現。 Graphviz 引擎如下： dot neato fdp twopi circo 其中 circo 和 neato 的效果較符合圖譜期望。 NetworkX 引擎如下： kamada kawai（有 SciPy 需求因此未加入） shell circular spring spectral random 其中較適合的為 shell，random 為隨機產生。 很遺憾的是，Windows x64 的 Python 無法安裝 PyGraphviz，因此 Pyslvs 目前只有 Ubuntu 版本提供 Graphviz 引擎。 而經測試，AppImage 技術由於只將 PyGraphviz 包入，端口程式庫仍然連接 Graphviz 程式庫，所以 Ubuntu 用戶必須安裝 Graphviz 。 sudo apt install graphviz 以下是瓦特與史帝芬生鍊用 neato 引擎排佈的結果。","tags":"開發","url":"./yuan_2017-12-10.html"},{"title":"Pyslvs v0.9 - 12/05","text":"拓樸排列程式 拓樸排列程式 花了一些時間寫了一個排列拓樸程式，將概念寫在這邊。 在論壇爬文時，看到作者自己推薦的 Python 樹狀結構模組 anytree，看了說明文件後決定使用此模組協助樹狀管理。 以一個四連桿 (4,) 的樹狀拓樸如下，只有一種排列方法： L0(2) ├── L1(2) │ └── L3(2) │ └── [L2](2) └── L2(2) └── [L3](2) ------- Answer count: 1 需要的模組有： from anytree import Node, RenderTree from anytree.search import findall from itertools import permutations from typing import Tuple 接著是印出上面樹狀結構的函式，anytree 的 RenderTree 搜尋函式會朝下列出節點的階級字元。 這邊用 noname 這個 bool 變數決定是否顯示名稱。 show_tree = lambda root: '\\n'.join(\"{}{}({})\".format(pre, n.name, n.limit) for pre, fill, n in RenderTree(root)) 接下來是主函式，稱為 make_link ，接收內含 int 的可迭代物件。 def make_link(iter: Tuple[int,]): ... return answer 第一部分是創出連桿的數量，數字則是接頭數。 link_type = [] for i, num in enumerate(iter): i += 2 for j in range(num): link_type.append(i) 如輸入 (4,) ，可以得到 [2, 2, 2, 2] ；輸入 (5, 4) 可得 [2, 2, 2, 2, 2, 3, 3, 3, 3] 。 使用 Python 迭代工具模組的 permutations 函式來創造排列組合的迴圈。 相符無誤的項目會將 root 節點加入答案，有錯誤則用 continue 關鍵字跳過。 answer = [] for all_link in list(set(permutations(link_type))): ... answer.append(links[0]) 首先轉換 link_type 的內容成為 anytree 模組的 Node 類型。 其中 limit 屬性是此節點的接頭上限，僅用於比對，並無程式上的限制。 all_link = [Node(\"L{}\".format(i), limit=v) for i, v in enumerate(all_link)] 接著將第一項當作 root 節點，加入 links 。 這裡 links 清單的最後一項 links[-1] 是接下來的搜索法準備填入的項目。 links = [] links.append(all_link.pop(0)) 然後使用廣度優先搜索法 (Breadth-First-Search, BFS) 填入所有節點，使用 list 類型的 pop 方法配上 while 迴圈可以確保用光所有節點。 當指派一個節點的 parent 屬性時，anytree 模組會自動將節點連上父節點，父節點可以透過 children 屬性取得一個裝有所有子節點指標的 tuple 物件。 while all_link: link = all_link.pop(0) if (len(links[-1].children) + bool(links[-1].parent))==links[-1].limit: links.append(links[-1].children[0]) link.parent = links[-1] 由於數學定義的「樹 (tree)」結構中，子節點只能擁有一個父項，否則為迴路 (Loop)，anytree 模組會在連接成迴路時自動回擲 LoopError 錯誤。 但是我們的運動鍊為 close chain，因此必須再創立一個配對流程，這次使用類似連結的概念，同時為「主體」連結一個虛擬節點。 虛擬節點的樣式使用中括弧 [ ] 辨識，不用指派名稱。 創立 get_no_done 函式回傳使用 anytree 的 findall 模組過濾沒配對完成的節點。 get_no_done = lambda: findall(links[0], filter_=lambda n: '[' not in n.name and (len(n.children) + bool(links[-1].parent)) < n.limit) error = False while get_no_done(): nodes = get_no_done() try: l_1, l_2 = nodes[0], nodes[1] except (ValueError, IndexError): error = True break else: Node(\"[{}]\".format(l_1.name), limit=str(l_1.limit), parent=l_2) Node(\"[{}]\".format(l_2.name), limit=str(l_2.limit), parent=l_1) 最後檢查是否在上述迴圈出現沒閉合狀況。 if error: continue 或是兩對連桿之間有連到一個以上的接頭。 if findall(links[0], filter_=lambda n: len([c.name for c in n.children])!=len(set(c.name for c in n.children))): continue 最後可以進行測試： if __name__=='__main__': print(\"Topologic test\") answer = topo([5, 4]) #Show tree for root in answer: print(show_tree(root)) print('-'*7) print(\"Answer count: {}\".format(len(answer))) 可得： ... ------- L0(2) ├── L1(3) │ ├── L3(2) │ │ └── L5(3) │ │ ├── L6(3) │ │ │ ├── L8(3) │ │ │ │ ├── [L6](3) │ │ │ │ └── [L7](2) │ │ │ └── [L8](3) │ │ └── L7(2) │ │ └── [L8](3) │ └── L4(2) │ └── [L2](2) └── L2(2) └── [L4](2) ------- Answer count: 60 經驗證，所有接頭都有連接。","tags":"開發","url":"./yuan_2017-12-05.html"},{"title":"Pyslvs v0.9 - 12/03","text":"PMKS 轉換式更新 機構範例 PMKS 轉換式更新 完成滑動接頭 P 與 RP 的轉換式，已經可以支援這兩種接頭的輸入。 另外改進了三點共線和共點在 Solvespace 輸入的錯誤。 機構範例 增加了兩個範例，用作測試上述程式。 曲柄滑塊 雙臂接球機構","tags":"開發","url":"./yuan_2017-12-03.html"},{"title":"設計、設計方法與機械設計","text":"從設計觀念的釐清, 到設計方法的探尋, 以及利用各種設計方法來進行機械設計, 到底有沒有一套脈絡或論述可以依循? 設計到底是甚麼? 在工程領域, 設計應該是一種表達, 而且是能夠讓參與設計的所有團隊成員都充分了解, 且據以依循, 可以得到預期結果的具體表達. 工程設計常用的表達至少有口語、文字、2D、3D、數學與實體等六種方式. 例如: 利用 Leo Editor 管理 Pelican 靜態網誌系統的協同使用\"設計\", 文字表達敘述如下: 這是一套允許多人協同編寫位於 content 目錄下的 Markdown 檔案格式或 reStructuredText 格式文章原稿的系統 為了完整保留本網誌系統原稿與設定檔案的歷程資料, 採用 Github 或 Fossil SCM 進行內容組態管理 為了在組態管理歷程資料過程, 避免各學員的 Leo Editor 專案 XML 檔案, 因合併產生衝突處理上的困難, 規定各成員必須自行維護管理 users 目錄下, 以作者名稱命名的 .leo 檔案 為了讓 Pelican 所產生的 html 網誌系統, 可以同時在無網路連線的近端與雲端上使用, 近端利用 pelicanconf.py 加上 local_publishconf.py 轉檔, 遠端則使用 pelicanconf.py 加上 publishconf.py 轉檔 Pelican 轉換完成的 html 檔案, 設定置於 blog 目錄中 由於 Pelican 轉換後的 html 位於 blog 子目錄, 因此整個系統根目錄中的 index.html 以 head 標註中的 meta redirect 跳轉至 blog 目錄中的 index.html 為了讓多人所建立的文章原稿, 同時存入 content 目錄而不會產生覆蓋, 規定以作者名稱加上底線, 再加上當天日期及副檔名命名 作者若同一天建立多篇文章原稿, 則以用戶名稱_日期-1.md 等 dash 後加上數字區別 因為 Pelican 針對沒有 slug 欄位設定的中文標題文章原稿, 會以拉丁拼音命名轉換後的 html 檔案, 比較不容易望文生義, 因此建議各文章以有意義的英文名稱命名, 且最前方加上作者名稱, 以避免因重複 slug 設定, 而讓 Pelican 無法轉檔 為了讓各用戶的 Leo Editor 文章節點中, 以 @edit 或 @clean 節點指令下的文章更容易查找, 建議在存檔節點的根節點, 以文章標題註記 有關 attila 樣板右方 menu 側欄中的連結增刪, 可以透過編輯 partials 目錄中的 navigation.html 達成 頁面正中方的搜尋表達, 以修改近端與雲端 templates 目錄中的 base.html 檔案中的 search section, 套入 search.html 達成 系統啟用 summary plugin 的目的, 在於讓 reStructuredText 格式文章原稿可以透過標註, 區隔摘要與內文 系統啟用 neighbors plugin 的目的, 在於讓各篇文章末端出現前後文章的連結, 以方便循序瀏覽閱讀 系統啟用 tipuesearch plugin 的目的, 在於讓使用者可以透過兩個字元以上的關鍵字進行全文搜尋 為了讓 Pelican 轉換完成的 html 檔案, 可以採 tipuesearch Javascript 延伸功能, 以關鍵字搜尋, 近端關鍵字以 tipuesearch_content.js 儲存, 遠端則使用 tipuesearch_content.json 儲存, 詳細內容可參見 plugin 目錄中, tipue_search 子目錄中的 tipue_search.py 設定 上述之所以在轉檔階段需要區分近端與雲端的原因, 在於近端無 disqus 設定, 而遠端則附加 disqus 回應系統 為了讓近端與遠端瀏覽器中各 AJAX 前後端程式系統的反應一致, 近端利用 www-server 按鈕, 以執行緒啟動 https 伺服器, 使用者可以在轉檔完成後, 以瀏覽器 IPv4 網路協定檢查內容 為了讓系統在 IPv6 網路協定下正常運作, 以 ipv6-https-server 按鈕, 以執行緒啟動 https 伺服器, 使用者可以在轉檔完成後 ,以瀏覽器 IPv6 網路協定檢查內容 當然, 本網誌系統的完整原始資料都保存在 Pyslvs 倉儲 , 任何人只要 git clone 倉儲, 稍加修改, 就可以另起爐灶, 延續這個網誌系統的價值, 但是其中許多細微精密的設計, 若沒有完整表達, 一旦爾後使用環境改變或各相關系統改版, 使用者就無法充分掌握各開放系統的互動搭配, 獨力配置因應. 換言之, 工程領域中與所謂設計相關的具體表達, 至少是時間與所處環境的函數, 一旦時空轉變, 就必須透過完整的歷程組態管理紀錄, 啟動各互動元件間的配置修改, 方能延續或加值原始設計的表達, 得到預期結果. 設計方法 假如我們接受在工程領域中, 上述所謂設計是一種表達的陳述, 那麼在表達設計的歷程中, 將存在許多解決問題的方法, 與所處時空背景的說明. 首先, 甚麼是方法? \"方\"為合乎約制條件, 可以實際拿出來使用的策略與規則, 表示並非空想, 而可實際施行的內容, 才叫\"方\". 至於\"法\"是順應自然條件下, 可因時空而制宜的最高行事準則. 因此\"方法\"就是: 配合不同條件, 實際施行的最高準則. 而再從上述設計有六種表達方式的論述出發, 那麼以口語表達而言的設計方法, 就是: 配合不同條件, 實際施行口語表達的最高準則. 也就是因應環境與對象, 將設計內容, 說清楚講明白所採行的策略與準則. 因此, 所謂設計方法, 除了口語表達外, 還可以從文字、2D、3D、數學與實體等表達的形式, 加以發揮, 具體呈現設計內容. 由於設計方法以各種形式表達的過程中, 會因時空背景與參與人員所做決策的差異, 而產生不同的結果, 多人協同團隊為了更有效掌握過程中的各項細節, 因此設計方法及組成元件有關的組態管理系統 (Configuration Management) 因應而生. 機械設計 機械是一種器物, 而且是由固體、流體與軟體元件精巧組合而成, 可互動運作, 達成特定功能之器物. 因此機械設計就是靈活運用六種表達方式, 明確說明如何透過固體、流體與軟體元件之互動運作, 而能達成預定結果之明確與具體表達. Pyslvs 是機械設計過程中的一項工具, 主要由平面機構模擬核心、演化運算核心與視窗圖形化介面程式所組成. 其中, 兩種運算核心都依據平面機構有關的數學模型與分析表達, 採用軟體元件製作, 再結合 2D 使用者圖形介面建立物件導向, 以及事件驅動程式元件等功能, 讓使用者可以輸入平面機構模型後, 進行模擬或合成運算. 而 Pyslvs 平面機構模擬核心的主體為一套 Geometric Constrain Solver, 依附在 Solvespace 參數化 3D 繪圖套件中. 在 2013 年 9 月透過 SWIG (Simplified Wrapper and Interface Generator) 技術, 轉為 Python2 可呼叫的程式庫, 為 Python2-Solvespace . 2016 年 7 月之後, 經本站轉為 Python3 可呼叫的程式庫, 成為 Python3-Solvespace . 至於 Pyslvs 平面機構合成所使用的演化運算核心 ,則源自 2015 年 4 月利用 Cython (C-extension for Python) 技術所開發的 Algorithm , 包含實數編碼基因 (Real-coded Genetic) 演算法、差分進化 (Differential Evolution) 演算法與螢火蟲 (Firefly) 演算法等模組. Pyslvs 的圖形介面採用 PyQt5 , 在 Eric6 整合開發環境中建立.","tags":"論述","url":"./scrum_design-design_methods-and-mechanical-design.html"},{"title":"Pyslvs v0.9 - 11/28","text":"介面操作重大更新 介面操作重大更新 今天改寫了一下畫布介面。 將拍照到剪貼簿的按鈕移到右上角的版本標籤旁；表格頁籤旁改成「全部選擇」按鈕。 新增兩個功能的快捷鍵： 全選點 (Select all point)：Ctrl + A 自由移動模式切換 (Free move mode toggle)：Ctrl + F 另外有一個重大突破：矩形窗選功能。 在非自由移動模式下可靠滑鼠拖拉矩形線框，選取畫布上的點。 自由移動模式下拖拉將會移動並修改選擇的點座標。","tags":"開發","url":"./yuan_2017-11-28.html"},{"title":"Pyslvs.com 上線","text":"2017.11.26 之前的 pyslvs 網站內容備份在 https://kmolyuan.github.io/pyslvs/ , 目前的 http://pyslvs.com 使用 http://pyslvs.github.io 作為網站內容, disqus 則登記為 pyslvs-com. 這項改變的目的是以 Pelican 靜態網頁取代原先的一頁式網頁, 除了比較容易維護之外, 也可以提供更充實的內容. 這項以 Github Pages 架構作為雲端 WWW 伺服器, 而 DNS 的設定首先是將 http://www.pyslvs.com 以 CNAME 指向 http://pyslvs.github.io , 然後在內定轉址的根網址 http://pyslvs.com , 以 301 類型轉至 http://www.pyslvs.com . 至於 Github Pages 的部分則是針對 https://github.com/pyslvs/pyslvs.github.io 倉儲, 將 Settings 中的 Custom Domain 設為 http://www.pyslvs.com 就算完成. Pyslvs 的原意為 Python for Solvespace , 是讓使用者容易使用 Solvespace 所開源出來的 Geometric Constraint Solver, 也就是 Python Solvespace , 隨後利用 PyQt5 使用者介面並加上演化合成引擎, 成為目前的 PSLVS (Python Synthesis of Linkages and Verification Software), 中文為 Python 機構合成與驗證套件, 其開發目標希望成為一套能夠用於機械產品平面機構合成與機構可用性驗證的模擬分析與最佳化設計套件. 其他開放源機構分析軟體: http://blog.rectorsquid.com/linkage-mechanism-designer-and-simulator/ (Github: https://github.com/rectorsquid/Linkage ) https://designengrlab.github.io/PMKS/ (Github: https://github.com/DesignEngrLab/PMKS )","tags":"論壇","url":"./pyslvs-on-line.html"}]};