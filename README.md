# learn-ai-ex2
Ex4: Read the entire file story.txt and write a program to print out top 100 words occur most
frequently and their corresponding appearance. You could ignore all
punction characters such as comma, dot, semicolon, ...
Sample output:
house: 453
dog: 440
people: 312
...

## Solution
- Xử lý data
  - Load file lên và chuyển tất cả thành chữ in thường, lọc ra các từ không dính kèm ký tự đặc biệt vào 1 list (ví dụ các từ dính kèm ký tự đặc biệt: "Alice's", "[EBook", "Author:", "19,"...)
  - Đối với từ dính kèm ký tự đặc biệt, dùng các hàm như replace(), split() để loại bỏ các ký tự, rồi append list này vào word_list (không dính kèm ký tự đặc biệt)
- Sau bước xử lý data, chỉ cần tạo 1 dictionary và đếm top 100 số lần xuất hiện nhiều nhất
