# The VH5000 Example

這份教材是透過五倍劵及加碼劵來學習 django web programming。

In **dj01** example, we demo how to develop a simple web by
* creating an app called bonus (加碼劵),
* *Model* design: Prize 獎品 and Winner 中獎號碼,
* Input data from the role of *administrator*, and from the *Shell*,
* *View* design: to see the Winner,
* *Template* design: based template design, extending template design, *template language* to show html and data from views.

In the **dj03** example, demo how to use class-based view
* Prize 新增 ImageField 來儲存 logo (存在 media 目錄)
* Prize 新增 desc 來儲存 描述
* 透過 Prize list view 來呈現 prize 的列表
* 透過 Prize detial view 來呈現個別 prize 的細節
