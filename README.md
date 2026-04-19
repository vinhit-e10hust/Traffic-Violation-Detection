# Traffic-Violation-Detection
Giới thiệu về bộ dữ liệu: Tổng quan

Một bộ dữ liệu được tuyển chọn tùy chỉnh được xây dựng để phát hiện vi phạm giao thông trong thế giới thực. Kết hợp dữ liệu từ 3 nguồn công khai trên 23 lớp với 5.254 hình ảnh huấn luyện và 1.470 hình ảnh xác thực ở định dạng YOLO tương thích với YOLOv8/v9/v12.

Nó giúp huấn luyện một mô hình duy nhất để phát hiện tất cả các đối tượng cần thiết cùng một lúc.

**Tính năng chính:** Các lớp phương tiện (người, ô tô, xe tải, xe buýt, xe máy) được trích xuất bằng cách cắt vùng quan tâm (ROI) — mỗi khung hình của phương tiện được cắt với phần đệm 30% và được lưu dưới dạng hình ảnh riêng lẻ. Điều này đảm bảo các phương tiện nổi bật trong khung hình và loại bỏ vấn đề không khớp tỷ lệ thường gặp khi kết hợp cảnh quay từ camera hành trình với hình ảnh biển báo cận cảnh.

**23 classes được phân loại:**

**Phương tiện:** người, ô tô, xe tải, xe buýt, xe máy

**Đèn giao thông:** đèn đỏ, đèn xanh

**Biển báo giao thông:** biển báo dừng, cấm vào, cấm vượt, cấm rẽ trái, cấm rẽ phải, cấm quay đầu, cấm dừng

**Giới hạn tốc độ:** giới hạn tốc độ 20, giới hạn tốc độ 30, giới hạn tốc độ 40, giới hạn tốc độ 50, giới hạn tốc độ 60, giới hạn tốc độ 70, giới hạn tốc độ 80, giới hạn tốc độ 100, giới hạn tốc độ 120

Format: Tương thích với YOLOv8/v9/v12 — hộp giới hạn xywh được chuẩn hóa, một tệp .txt cho mỗi hình ảnh. ID lớp nhất quán trên tất cả các lần chia.
Dataset: https://drive.google.com/drive/folders/1veha4vzVGt8jDNu7rNqr9EHsCAp9fobZ
