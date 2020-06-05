# CTPN-use-labelImg-text-label-fast

reqiured :
labelImg tool 
https://github.com/tzutalin/labelImg.git



because the endless labeling CTPN text labels , this code will split large (long) rectbox into small 16 pix width rectbox 
that all the text label need

因為標註CTPN資料標籤需要不斷的框出16像素寬的文字框，標註大量文字框的時候非常痛苦與無奈，所以這支程式可以將長的文字框，切割成寬度16的文字框

說明 :
程式會將標註為 textbox 的文字框都切割，但是標註為 text 的都不會動，而且只會做 VOC 格式的 XML，因為我只需要這個


