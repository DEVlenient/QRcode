# QRCode 生成器

這個程式是一個簡單的 QRCode 生成器，讓您可以輕鬆地生成包含網址的 QRCode 圖片。您可以自定義網址和圖片名稱，並選擇儲存的位置。

## 功能簡介

- 輸入要生成 QRCode 的網址。
- 輸入要儲存 QRCode 圖片的名稱。
- 選擇要儲存的位置。
- 生成 QRCode 圖片並保存到指定位置。
- 如果輸入的名稱不合法，則提示錯誤信息。

## 範例演示

<img src="pic/qrcode.gif" alt="示例圖片" width="600">

## 使用方法

1. 運行程式，您將會看到一個簡單的視窗。
2. 在 "請輸入要生成 QRCode 的網址：" 欄位中，輸入您要生成 QRCode 的網址。
3. 在 "請輸入要儲存 QRCode 的名稱：" 欄位中，輸入您希望儲存 QRCode 圖片的名稱（不包含副檔名）。
4. 點擊 "選擇儲存位置" 按鈕，選擇您希望儲存 QRCode 圖片的文件夾位置。
5. 點擊 "生成 QRcode" 按鈕，程式將生成 QRCode 圖片並儲存到指定位置。

## 安裝與執行

1. 下載程式源碼或執行檔。
2. 在命令提示字元或終端機中，進入程式所在的資料夾。
3. 安裝必要的套件，執行以下指令：
    ```
    pip install numpy
    ```
    ```
    pip install numpy
    ```
4. 執行程式：
    ```
    python qr_creator.py
    ```

## 開發環境

- 所需程式語言：Python
- 所需導入模組：qrcode、os、pathlib、tkinter、filedialog、messagebox

## 授權訊息

這個程式遵循 [MIT 授權](LICENSE.txt)，您可以自由地使用、修改和分享這個程式。
