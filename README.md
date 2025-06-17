# Chương Trình Giải Mê Cung (Maze Solver)

## Cách cài đặt và sử dụng
1. Clone dự án từ GitHub:
   ```
   git clone https://github.com/vinhdangtapcode/MazeGamePython.git
   cd MazeSolver
   ```

2. Cài đặt thư viện Pygame:
   ```
   pip install pygame
   ```

3. Chạy chương trình:
   ```
   python maze_game.py
   ```

4. Sử dụng chương trình:
   - Nhấp vào "Generate Maze" để tạo mê cung mới
   - Chọn kích thước mê cung mong muốn (10x10, 20x20, 50x50)
   - Nhấp vào các nút thuật toán để xem cách mỗi thuật toán giải quyết mê cung
   - Quan sát quá trình khám phá (màu xanh dương) và đường đi cuối cùng (màu vàng)
   - Nhấp "Reset" để tạo mê cung mới

## Tổng Quan
Đây là ứng dụng đồ họa giúp trực quan hóa và so sánh các thuật toán tìm đường trong mê cung. Người dùng có thể tạo mê cung ngẫu nhiên với nhiều kích thước khác nhau và quan sát cách các thuật toán khác nhau giải quyết vấn đề.

## Các thuật toán được triển khai
- **A\* (A-star)**: Thuật toán tìm đường tối ưu sử dụng hàm heuristic và chi phí đường đi, thường tìm ra đường đi ngắn nhất.
- **Greedy (Tham lam)**: Thuật toán chỉ sử dụng hàm heuristic để ước tính khoảng cách đến đích, không xem xét chi phí đường đi.
- **BFS (Breadth-First Search)**: Thuật toán tìm kiếm theo chiều rộng, khám phá tất cả các nút ở cùng một mức trước khi đi sâu hơn.
- **DFS (Depth-First Search)**: Thuật toán tìm kiếm theo chiều sâu, khám phá một đường đi càng sâu càng tốt trước khi quay lại.

## Chức năng chính
- Tạo mê cung ngẫu nhiên với kích thước khác nhau (10x10, 20x20, 50x50)
- Hiển thị quá trình khám phá và giải pháp của mỗi thuật toán
- So sánh hiệu suất giữa các thuật toán (độ dài đường đi, số lượng ô đã khám phá)
- Lưu lại kết quả các lần chạy thuật toán để so sánh

## Giao diện người dùng
- Nút kích thước: Để chọn kích thước mê cung (10x10, 20x20, 50x50)
- Các nút thuật toán: A*, Greedy, DFS, BFS để chạy từng thuật toán
- Nút Reset: Để tạo mê cung mới
- Bảng kết quả: Hiển thị thông tin về các thuật toán đã chạy

## Kiểm thử hiệu suất
File `test.py` được dùng để kiểm tra hiệu suất của các thuật toán trên nhiều mê cung khác nhau. Khi chạy file này, chương trình sẽ:
- Tạo 30 mê cung khác nhau (cỡ 50x50) với 3 bố cục điểm bắt đầu và kết thúc khác nhau
- Chạy cả 4 thuật toán trên mỗi mê cung
- Ghi lại độ dài đường đi, số lượng ô khám phá và thời gian thực thi
- Lưu kết quả vào các file CSV: path.csv, node.csv, time.csv

## Cấu trúc dự án
- `maze_game.py`: File chính chứa giao diện đồ họa và logic chương trình
- `maze.py`: Chứa các lớp và thuật toán liên quan đến mê cung
- `test.py`: Công cụ kiểm tra hiệu suất và tạo báo cáo
- `*.csv`: File kết quả kiểm tra hiệu suất

## Yêu cầu hệ thống
- Python 3.x
- Thư viện Pygame

## Tài liệu tham khảo
- AI-Intro HUST Slides
- https://github.com/trinhhgiang/MazeSolver