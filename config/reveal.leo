<?xml version="1.0" encoding="utf-8"?>
<!-- Created by Leo: http://leoeditor.com/leo_toc.html -->
<leo_file xmlns:leo="http://leoeditor.com/namespaces/leo-python-editor/1.1" >
<leo_header file_format="2"/>
<globals/>
<preferences/>
<find_panel_settings/>
<vnodes>
<v t="leo.20180902120538.1"><vh>@settings</vh>
<v t="leo.20180902120538.2"><vh>@data qt-gui-plugin-style-sheet</vh></v>
<v t="leo.20180902120538.3"><vh>@string initial_split_orientation = horizontal</vh></v>
</v>
<v t="leo.20180902120523.1"><vh>編輯 reveal</vh>
<v t="leo.20180902120523.2"><vh>@path ./../reveal</vh>
<v t="leo.20180902120523.3"><vh>@clean index.html</vh>
<v t="leo.20180902120523.4"><vh>html</vh>
<v t="leo.20180902120523.5"><vh>head</vh></v>
<v t="leo.20180902120523.6"><vh>body</vh>
<v t="leo.20180902120523.7"><vh>reveal div</vh>
<v t="leo.20180902120523.8"><vh>slides div</vh>
<v t="leo.20180902120523.9"><vh>封面</vh></v>
<v t="leo.20210520133953.1"><vh>架構介紹</vh>
<v t="leo.20210520133953.3"><vh>目錄</vh></v>
<v t="leo.20210520134352.2"><vh>研究動機</vh></v>
<v t="leo.20210520134138.2"><vh>研究流程</vh></v>
</v>
<v t="leo.20210520134443.1"><vh>平面多連桿機構套件</vh>
<v t="leo.20210520140725.2"><vh>平面多連桿機構套件轉場</vh></v>
<v t="leo.20210520134443.3"><vh>套件比較</vh></v>
<v t="leo.20210520134443.5"><vh>Pyslvs_UI介紹</vh></v>
</v>
<v t="leo.20210520135544.1"><vh>機構合成</vh>
<v t="leo.20210520140311.2"><vh>機構合成轉場</vh></v>
<v t="leo.20210521110904.1"><vh>評量介紹</vh></v>
<v t="leo.20210521111034.3"><vh>評量影片</vh></v>
<v t="leo.20210520135544.5"><vh>尺寸合成</vh></v>
<v t="leo.20210520135544.7"><vh>量化評比</vh></v>
</v>
<v t="leo.20210520141042.1"><vh>延伸應用</vh>
<v t="leo.20210520150420.2"><vh>轉場</vh></v>
<v t="leo.20210520141042.3"><vh>3D零件</vh></v>
<v t="leo.20210520141042.5"><vh>CoppeliaSim動態模擬軟體</vh></v>
<v t="leo.20210520141042.7"><vh>CoppeliaSim API</vh></v>
</v>
<v t="leo.20210520141843.1"><vh>結論</vh>
<v t="leo.20210520141843.3"><vh>結論內容</vh></v>
<v t="leo.20210520141843.5"><vh>感謝聆聽</vh></v>
</v>
<v t="leo.20180902120523.13"><vh>各式內容引用範例</vh>
<v t="leo.20210520142259.1"><vh>導入圖片</vh>
<v t="leo.20210520142259.2"><vh>導入圖片</vh></v>
</v>
<v t="leo.20180902120523.14"><vh>導入數學符號與方程式</vh>
<v t="leo.20180902120523.15"><vh>LaTeX 格式方程式</vh></v>
</v>
<v t="leo.20180902120523.16"><vh>導入縮排程式碼</vh>
<v t="leo.20180902120523.17"><vh>引用程式碼</vh></v>
</v>
<v t="leo.20180902120523.18"><vh>導入影片</vh>
<v t="leo.20180902120523.19"><vh>iframe 導入影片</vh></v>
</v>
</v>
<v t="leo.20180902120523.11"><vh>快捷鍵</vh>
<v t="leo.20180902120523.12"><vh>投影片快捷鍵</vh></v>
</v>
</v>
</v>
</v>
</v>
</v>
</v>
</v>
</vnodes>
<tnodes>
<t tx="leo.20180902120523.1"></t>
<t tx="leo.20180902120523.11">&lt;section data-markdown&gt;
    &lt;script type="text/template"&gt;
@others
    &lt;/script&gt;
&lt;/section&gt;


						
</t>
<t tx="leo.20180902120523.12"># 投影片快捷鍵

* 利用箭頭上下前後換頁
* 按 f 鍵進入全螢幕模式 (full screen)
* 按 s 鍵可以顯示投影片筆記 (show)
* 按 o 鍵可以切換單張或全域檢視 (overview)
* 按 b 或 . 鍵可以切換螢幕黑屏 (black)
* 按 Esc 可以退出全螢幕或全域檢視 (Escape)

</t>
<t tx="leo.20180902120523.13">&lt;section&gt;
@others
&lt;/section&gt;

</t>
<t tx="leo.20180902120523.14">&lt;section data-markdown&gt;
    &lt;script type="text/template"&gt;
&lt;!-- 請注意, @others 不可以內縮 --&gt;
@others
    &lt;/script&gt;
&lt;/section&gt;



						
</t>
<t tx="leo.20180902120523.15"># 數學符號與方程式

Inline math equations go in like so: $\omega = d\phi / dt$. Display
math should get its own line and be put in in double-dollarsigns:

$$I = \int \rho R^{2} dV$$
</t>
<t tx="leo.20180902120523.16">&lt;section data-markdown&gt;
    &lt;script type="text/template"&gt;
&lt;!-- 請注意, @others 不可以內縮 --&gt;
@others
    &lt;/script&gt;
&lt;/section&gt;



						
</t>
<t tx="leo.20180902120523.17">## 利用 Markdown 寫投影片
以下利用 Markdown 格式展示 Python 程式碼:
```
@language python
# use threading and subprocess to threading the make process
import os
import subprocess
import threading

def domake():
    
    path = "../exposed/api/exposed"
    ubuntu = "../Ubuntu"
    
    # create obj path
    
    if not os.path.exists(path+"/../obj"):
        os.makedirs(path+"/../obj")
    
    subprocess.call(["make", "clean"], cwd=path)
    subprocess.call("make", cwd=path)
    subprocess.call(["cp", "{libslvs.so, _slvs.so, slvs.py}", ubuntu], cwd=path)
    subprocess.call(["python3", "circle_ex.py"], cwd=path+"/"+ubuntu)
    
make = threading.Thread(target=domake)
make.start()
```
</t>
<t tx="leo.20180902120523.18">&lt;section data-markdown&gt;
    &lt;script type="text/template"&gt;
@others
    &lt;/script&gt;
&lt;/section&gt;


						
</t>
<t tx="leo.20180902120523.19">## 使用 iframe 導入影片

### 導入影片 template

&lt;iframe src="https://player.vimeo.com/video/183950627" width="640" height="492" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen&gt;&lt;/iframe&gt;
</t>
<t tx="leo.20180902120523.2"></t>
<t tx="leo.20180902120523.3">@language xml
@tabwidth -4
@others

</t>
<t tx="leo.20180902120523.4">&lt;!doctype html&gt;
&lt;html lang="en"&gt;
@others
&lt;/html&gt;
</t>
<t tx="leo.20180902120523.5">&lt;head&gt;
    &lt;meta charset="utf-8"&gt;
&lt;title&gt;
Pyslvs-UI 平面多連桿機構套件之合成與應用
&lt;/title&gt;
    &lt;meta name="description" content="A framework for easily creating beautiful presentations using HTML"&gt;
    &lt;meta name="author" content="Hakim El Hattab"&gt;
    
    &lt;meta name="apple-mobile-web-app-capable" content="yes"&gt;
    &lt;meta name="apple-mobile-web-app-status-bar-style" content="black-translucent"&gt;
    
    &lt;meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no"&gt;
    
    &lt;link rel="stylesheet" href="css/reveal.css"&gt;
    &lt;link rel="stylesheet" href="css/theme/black.css" id="theme"&gt;
    
    &lt;!-- Theme used for syntax highlighting of code --&gt;
    &lt;link rel="stylesheet" href="lib/css/zenburn.css"&gt;

    &lt;!-- Printing and PDF exports --&gt;
    &lt;script&gt;
        var link = document.createElement( 'link' );
        link.rel = 'stylesheet';
        link.type = 'text/css';
        link.href = window.location.search.match( /print-pdf/gi ) ? 'css/print/pdf.css' : 'css/print/paper.css';
        document.getElementsByTagName( 'head' )[0].appendChild( link );
    &lt;/script&gt;

    &lt;!--[if lt IE 9]&gt;
    &lt;script src="lib/js/html5shiv.js"&gt;&lt;/script&gt;
    &lt;![endif]--&gt;
&lt;/head&gt;

</t>
<t tx="leo.20180902120523.6">&lt;body&gt;
@others
&lt;script src="lib/js/head.min.js"&gt;&lt;/script&gt;
&lt;script src="js/reveal.js"&gt;&lt;/script&gt;
&lt;script&gt;
        // More info https://github.com/hakimel/reveal.js#configuration
        Reveal.initialize({
            controls: true,
            progress: true,
            history: true,
            center: true,

            transition: 'slide', // none/fade/slide/convex/concave/zoom

            // More info https://github.com/hakimel/reveal.js#dependencies
            dependencies: [
                { src: 'lib/js/classList.js', condition: function() { return !document.body.classList; } },
                { src: 'plugin/markdown/marked.js', condition: function() { return !!document.querySelector( '[data-markdown]' ); } },
                { src: 'plugin/markdown/markdown.js', condition: function() { return !!document.querySelector( '[data-markdown]' ); } },
                { src: 'plugin/highlight/highlight.js', async: true, callback: function() { hljs.initHighlightingOnLoad(); } },
                { src: 'plugin/zoom-js/zoom.js', async: true },
                { src: 'plugin/notes/notes.js', async: true },
                { src: 'plugin/math/math.js', async: true }
            ]
        });
&lt;/script&gt;
&lt;/body&gt;

</t>
<t tx="leo.20180902120523.7">&lt;div class="reveal"&gt;
@others
&lt;/div&gt;

</t>
<t tx="leo.20180902120523.8">&lt;!-- Any section element inside of this container is displayed as a slide --&gt;
&lt;div class="slides"&gt;
@others
&lt;/div&gt;

</t>
<t tx="leo.20180902120523.9">&lt;section data-background="#dddddd"&gt;
    &lt;h2&gt;Pyslvs-UI 平面多連桿機構套件之合成與應用&lt;/h2&gt;


    &lt;small&gt;
    Created by &lt;a href="http:/lab.kmol.info"&gt;KMOLab&lt;/a&gt;
    &lt;/small&gt;
&lt;/section&gt;


						
</t>
<t tx="leo.20180902120538.1"></t>
<t tx="leo.20180902120538.2">QTreeWidget {
    /* These apply to the selected item, but not to editing items.*/
    background-color: #ffffec; /* Leo's traditional tree color */
    selection-color: black; /* was white */
    selection-background-color: lightgrey;
    /* font-family: SansSerif; */
    /*font-family: DejaVu Sans Mono;*/
    font-family:YaHei Mono;
    /* 標題字型大小設定 */
    font-size: 20px;
    font-weight: normal; /* normal,bold,100,..,900 */
    font-style: normal; /* normal, italic,oblique */
 }

/* Headline edit widgets */
QTreeWidget QLineEdit {
    background-color: cornsilk;
    selection-color: white;
    selection-background-color: blue;
    /*font-family: DejaVu Sans Mono;*/    
    font-family:YaHei Mono;
    /* 沒有特別對應字型大小 */
    font-size: 20px;
    font-weight: normal; /* normal,bold,100,..,900 */
    font-style: normal; /* normal, italic,oblique */
}

/* The log panes */
QTextEdit {
    background-color: #f2fdff;
    selection-color: red;
    selection-background-color: blue;
    /* font-family: Courier New; */
    font-family:YaHei Mono;
    /* log font 大小 */
    font-size: 20px;
    font-weight: normal; /* normal,bold,100,..,900 */
    font-style: normal; /* normal, italic,oblique */
}

/* The body pane */
QTextEdit#richTextEdit {
    background-color: #fdf5f5; /* A kind of pink. */
    selection-color: white;
    selection-background-color: red;
    /*font-family: DejaVu Sans Mono;*/
    /* font-family: Courier New; */
    font-family:YaHei Mono;
    /* 內文字型大小 */
    font-size: 20px;
    font-weight: normal; /* normal,bold,100,..,900 */
    font-style: normal; /* normal,italic,oblique */
}

QLabel {
    font-family:YaHei Mono;'CherryPy', 'pytz', 'mako', 'beautifulsoup4', 'pymysql', 'peewee'
    /* 下方的 Minibuffer 標題字型大小 */
    font-size: 20px;
    font-weight: normal; /* normal,bold,100,..,900 */
    font-style: normal; /* normal,italic,oblique */
}

/* Editor labels */
QLineEdit#editorLabel {
    background-color: #ffffec;
    font-family:YaHei Mono;
    /* 沒有直接對應字型大小 */
    font-size: 20px;
    font-weight: normal; /* normal,bold,100,..,900 */
    font-style: normal; /* normal,italic,oblique */
    border: 2px;
    margin: 2px;
}</t>
<t tx="leo.20180902120538.3">horizontal: body pane to the left
vertical: body pane on the botton</t>
<t tx="leo.20210520133953.1">&lt;section&gt;
@others
&lt;/section&gt;

</t>
<t tx="leo.20210520133953.3">&lt;section&gt;
    &lt;h2&gt;目錄&lt;/h2&gt;
    &lt;ul&gt;
        &lt;li&gt;研究動機&lt;/li&gt;
        &lt;li&gt;研究流程&lt;/li&gt;
        &lt;li&gt;平面多連桿機構套件&lt;/li&gt;
        &lt;li&gt;機構合成&lt;/li&gt;
        &lt;li&gt;延伸應用&lt;/li&gt;
        &lt;li&gt;結論&lt;/li&gt;
    &lt;/ul&gt;
&lt;/section&gt;
</t>
<t tx="leo.20210520134138.2">&lt;section data-background="#FFFFFF"&gt;
    &lt;h2&gt;研究流程&lt;/h2&gt;
    &lt;p&gt;研究架構圖&lt;/p&gt;
    &lt;img src="https://github.com/mdecourse/4072pj3/blob/master/project3/latex/%E6%9E%B6%E6%A7%8B%E5%9C%96.png?raw=true" alt="alt text" width="1000"/&gt;

&lt;/section&gt;
</t>
<t tx="leo.20210520134352.2">&lt;section&gt;
    &lt;/h2&gt;研究動機
    &lt;p&gt;
隨著科技越來越發達網路上有許多機構分析的套件，但是鮮少有機構合成功能的套件，且大多無公開原始碼。而本專題所使用的套件Pyslvs-UI 為本研究室所開發的套件且有公開原始碼，因此本專題利用該套件合成及模擬功能並以一登山車後避震機構為例。
    &lt;/p&gt;
&lt;/section&gt;
</t>
<t tx="leo.20210520134443.1">&lt;section&gt;
@others
&lt;/section&gt;

</t>
<t tx="leo.20210520134443.3">&lt;section&gt;
    &lt;h2&gt;平面多連桿機構套件比較&lt;/h2&gt;
    &lt;small&gt;
    與市面上已經有的套件進行比較
    &lt;/small&gt;
    &lt;img src="https://github.com/mdecourse/4072pj3/blob/master/project3/latex/%E5%A5%97%E4%BB%B6%E6%AF%94%E8%BC%83%E8%A1%A8%E6%A0%BC.jpg?raw=true" alt="alt text" width="800"/&gt;

&lt;/section&gt;
</t>
<t tx="leo.20210520134443.5">&lt;section&gt;
    &lt;h2&gt;Pyslvs-UI架構&lt;/h2&gt;
    &lt;small&gt;
    採用系統動機
    &lt;/small&gt;
    &lt;ul&gt;
        &lt;li&gt;平面多連桿機構設計分析之開放源套件系統&lt;/li&gt;
        &lt;li&gt;結構合成&lt;/li&gt;
        &lt;li&gt;驗證機構運動模擬&lt;/li&gt;

    &lt;/ul&gt;

    &lt;small&gt;
    Pyslvs架構背景
    &lt;/small&gt;
    &lt;/br&gt;
&lt;!--URL連結圖片比較不會跑掉--&gt;
    &lt;img src="https://github.com/mdecourse/4072pj3/blob/master/project3/latex/Pyslvs%E6%9E%B6%E6%A7%8B%E8%83%8C%E6%99%AF.png?raw=true" alt="alt text" width="480"/&gt;

&lt;!--&lt;/small&gt;
Pyslvs架構背景
&lt;small&gt;
 * Cython程式語言進行編譯成機構合成延伸做演算
 * SWIG使Python可呼叫C語言動態連結庫以建構平面連桿機構模擬作業系統 
 * PyQt5可將程式編譯內容後轉換成GUI圖形化介面--&gt;
&lt;/section&gt;

</t>
<t tx="leo.20210520135544.1">&lt;section&gt;
@others
&lt;/section&gt;

</t>
<t tx="leo.20210520135544.5">&lt;section&gt;
    &lt;h2&gt;尺寸合成&lt;/h2&gt;
    &lt;img src="https://github.com/mdecourse/4072pj3/blob/master/project3/latex/DEflow.png?raw=true" alt="alt text" width="380" height="500" align="left"/&gt;

&lt;/section&gt;
</t>
<t tx="leo.20210520135544.7">&lt;section&gt;
    &lt;h2&gt;後避震機構量化分析&lt;/h2&gt;
    &lt;p&gt;Anti-squat 量化分析&lt;/p&gt;


    &lt;img src="https://github.com/mdecourse/4072pj3/blob/master/project3/latex/%E9%87%8F%E5%8C%96%E8%A9%95%E6%AF%94_anti_squat_x.png?raw=true" alt="alt text" width="1000"/&gt;
&lt;/section&gt;
</t>
<t tx="leo.20210520140311.2">&lt;section&gt;
    &lt;h2&gt;機構合成&lt;/h2&gt;
&lt;/section&gt;
</t>
<t tx="leo.20210520140725.2">&lt;section&gt;
    &lt;h2&gt;平面多連桿機構套件&lt;/h2&gt;
&lt;/section&gt;

</t>
<t tx="leo.20210520141042.1">&lt;section&gt;
@others
&lt;/section&gt;

</t>
<t tx="leo.20210520141042.3">&lt;section&gt;
    &lt;h2&gt;3D零件自動生成&lt;/h2&gt;



    &lt;img src="https://github.com/mdecourse/4072pj3/blob/master/project3/latex/3D%E9%9B%B6%E4%BB%B6%E7%94%9F%E6%88%90.png?raw=true" alt="alt text" width="600"/&gt;
&lt;/section&gt;
</t>
<t tx="leo.20210520141042.5">&lt;section&gt;
    &lt;h2&gt;CoppeliaSim動態模擬軟體&lt;/h2&gt;
    &lt;ul&gt;
        &lt;li&gt;使用XML檔來匯入零件&lt;/li&gt;
        &lt;li&gt;可減少手動匯入的程序&lt;/li&gt;
        &lt;li&gt;快速調整所需參數&lt;/li&gt;
    &lt;/ul&gt;
    &lt;br&gt;
    &lt;iframe width="580" height="315" src="https://www.youtube.com/embed/JFDAjE7lJW8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen&gt;&lt;/iframe&gt;


&lt;/section&gt;
</t>
<t tx="leo.20210520141042.7">&lt;section&gt;
    &lt;h2&gt;CoppeliaSim遠端API&lt;/h2&gt;
    &lt;p&gt;遠端API功能介紹&lt;/p&gt;
    &lt;ul&gt;&lt;small&gt;
        &lt;li&gt;模擬組合件之避震器在行進時的實際狀況&lt;/li&gt;
        &lt;li&gt;遠端API便於Debug程式操作模擬、不須手動設定旋轉軸轉速&lt;/li&gt;
    &lt;/small&gt;&lt;/ul&gt;

    &lt;p&gt;遠端API程式架構&lt;/p&gt;

    &lt;img src="https://github.com/mdecourse/4072pj3/blob/master/project3/latex/coppeliasim%20API.png?raw=true" alt="alt text" width="550"/&gt;

&lt;/section&gt;
</t>
<t tx="leo.20210520141843.1">&lt;section&gt;
@others
&lt;/section&gt;

</t>
<t tx="leo.20210520141843.3">&lt;section&gt;
    &lt;h2&gt;結論&lt;/h2&gt;


    &lt;img src="https://github.com/mdecourse/4072pj3/blob/master/project3/latex/follow-up%20research.png?raw=true" alt="alt text" width="1000"/&gt;
&lt;/section&gt;

</t>
<t tx="leo.20210520141843.5">&lt;section&gt;
    &lt;h2&gt;Thank you for listening&lt;/h2&gt;
&lt;/section&gt;
</t>
<t tx="leo.20210520142259.1">&lt;section data-markdown&gt;
    &lt;script type="text/template"&gt;
@others
    &lt;/script&gt;
&lt;/section&gt;


						
</t>
<t tx="leo.20210520142259.2">### 導入圖片 template

 &lt;!--URL連結圖片比較不會跑掉--&gt;
&lt;img src="https://github.com/mdecourse/4072pj3/blob/master/project3/latex/anti-squat_x-.png?raw=true" alt="alt text" width="200"/&gt;
</t>
<t tx="leo.20210520150420.2">&lt;section&gt;
    &lt;h2&gt;延伸應用&lt;/h2&gt;
&lt;/section&gt;
</t>
<t tx="leo.20210521110904.1">&lt;section&gt;
    &lt;h2&gt;登山車後避震機構評量&lt;/h2&gt;
    
    
    &lt;p align="left"&gt;Anti-rise (防後升):&lt;/p&gt;
    &lt;img src="https://media1.tenor.com/images/50aeb46deae11e8db0067cf3de78db4a/tenor.gif?itemid=17730464 alt="Flowers in Chania" align="right" width="400" height="200"&gt;&lt;/p&gt;
    &lt;small align="right"&gt;煞車時避震器抵抗上升力的能力&lt;/small&gt;
    
    &lt;br&gt;&lt;br&gt;&lt;br&gt;
    
    &lt;p align="left"&gt;Anti-squat (防後沉):&lt;/p&gt;
    &lt;small align="left"&gt;加速時避震器抵抗下壓力的能力&lt;/small&gt;
    &lt;img src="https://media1.tenor.com/images/ac1590317c0995871256ad29604aa686/tenor.gif?itemid=3404898" alt="Flowers in Chania" align="right" width="400" height="200"&gt;
    
&lt;/section&gt;







</t>
<t tx="leo.20210521111034.3">&lt;section&gt;
    &lt;h2&gt;登山車後避震機構評量&lt;/h2&gt;
    &lt;iframe width="560" height="315" align="left" src="https://www.youtube.com/embed/d4oySS3ZMD8?start=67" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen&gt;&lt;/iframe&gt;

&lt;/section&gt;
</t>
</tnodes>
</leo_file>
