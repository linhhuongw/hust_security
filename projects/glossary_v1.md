# THUẬT NGỮ (GLOSSARY) – BÁO CÁO BẢO MẬT DNS

Tài liệu này tổng hợp các thuật ngữ chính xuất hiện trong các chương của báo cáo, kèm giải thích ngắn gọn để các thành viên thống nhất cách hiểu và cách dùng khi viết nội dung.

---

## Chương 1: Cơ sở lý thuyết

- **DNS (Domain Name System – Hệ thống phân giải tên miền)**: Hệ thống phân cấp dùng để chuyển đổi (phân giải) tên miền dễ đọc (ví dụ `example.com`) thành địa chỉ IP mà máy tính sử dụng để định tuyến.
- **Root server (máy chủ gốc)**: Lớp cao nhất trong cây phân cấp DNS, biết vị trí của các máy chủ TLD.
- **TLD (Top-Level Domain – Tên miền cấp cao nhất)**: Phần cuối của tên miền, ví dụ `.com`, `.vn`, `.org`.
- **Authoritative DNS server (máy chủ DNS có thẩm quyền)**: Máy chủ lưu trữ bản ghi gốc (zone file) cho một tên miền cụ thể và trả về câu trả lời chính thức.
- **Recursive resolver (máy chủ phân giải đệ quy)**: Máy chủ thay mặt client thực hiện toàn bộ chuỗi truy vấn (root → TLD → authoritative) để trả về kết quả cuối cùng.
- **Zone file (tệp vùng)**: Tệp văn bản chứa các bản ghi DNS (resource records) của một zone (vùng quản lý tên miền).
- **Resource Record – RR (bản ghi tài nguyên)**: Đơn vị dữ liệu trong DNS, ví dụ A, AAAA, CNAME, MX, NS, TXT, SOA.
- **Cache (bộ nhớ đệm DNS)**: Nơi lưu tạm kết quả phân giải để tăng tốc các truy vấn lặp lại, có thời gian sống gọi là TTL (Time To Live).
- **Recursive query (truy vấn đệ quy)**: Truy vấn mà resolver phải tự đi tìm câu trả lời đầy đủ thay cho client.
- **Iterative query (truy vấn lặp)**: Truy vấn mà server chỉ trả về địa chỉ của server kế tiếp cần hỏi, không tự tìm tiếp.

---

## Chương 2: Lỗ hổng bảo mật của DNS

- **Lỗ hổng bảo mật (Vulnerability)**: Điểm yếu trong thiết kế, cấu hình hoặc triển khai của giao thức/hệ thống DNS có thể bị khai thác.
- **Khai thác (Exploit)**: Hành động hoặc công cụ lợi dụng lỗ hổng để gây ra hậu quả không mong muốn (đánh cắp dữ liệu, gián đoạn dịch vụ...).
- **Giao thức UDP/TCP trong DNS**: DNS chủ yếu dùng UDP (port 53) cho truy vấn thông thường vì tốc độ nhanh, nhưng UDP dễ bị giả mạo nguồn (spoofing) hơn TCP.
- **Plaintext (truyền văn bản rõ)**: Đặc điểm DNS truyền thống không mã hóa, khiến dữ liệu truy vấn có thể bị nghe trộm hoặc sửa đổi.

---

## Chương 3: Các hình thức tấn công DNS

- **Zero-day attack (Tấn công Zero-day)**: Tấn công khai thác lỗ hổng chưa được công bố hoặc chưa có bản vá, khiến hệ thống không có thời gian chuẩn bị phòng vệ.
- **Cache poisoning (Làm độc bộ nhớ cache / DNS Spoofing)**: Kẻ tấn công chèn bản ghi giả vào cache của resolver, khiến người dùng bị chuyển hướng đến địa chỉ IP độc hại khi truy vấn tên miền hợp lệ.
- **DDoS – Distributed Denial of Service (Tấn công từ chối dịch vụ phân tán)**: Sử dụng nhiều máy (botnet) đồng loạt gửi lượng lớn truy vấn đến máy chủ DNS để làm quá tải, gây gián đoạn dịch vụ phân giải tên miền.
- **DNS amplification (Tấn công khuếch đại DNS)**: Một dạng DDoS, kẻ tấn công gửi truy vấn nhỏ với địa chỉ nguồn giả mạo (của nạn nhân) đến các máy chủ DNS mở, khiến máy chủ trả về phản hồi lớn hơn nhiều lần tới nạn nhân.
- **Fast-flux DNS (DNS đổi IP nhanh)**: Kỹ thuật đổi địa chỉ IP gắn với một tên miền liên tục trong thời gian ngắn (TTL rất thấp), thường dùng để che giấu máy chủ điều khiển botnet hoặc lừa đảo, gây khó khăn cho việc chặn/điều tra.
- **DNS tunneling (Tạo đường hầm DNS)**: Kỹ thuật nhúng dữ liệu (lệnh điều khiển, dữ liệu đánh cắp...) vào trong các truy vấn/phản hồi DNS để vượt qua tường lửa hoặc lọc mạng.
- **DNS Hijacking (Chiếm đoạt DNS)**: Kẻ tấn công thay đổi cấu hình DNS (tại resolver, router, registrar hoặc thiết bị người dùng) để chuyển hướng truy vấn đến máy chủ do chúng kiểm soát.
- **MITM – Man-in-the-Middle Attack (Tấn công người ở giữa)**: Kẻ tấn công chặn và có thể sửa đổi luồng truy vấn/phản hồi DNS giữa client và server mà hai bên không hề biết.
- **Typosquatting (Chiếm đoạt tên miền qua lỗi chính tả)**: Đăng ký các tên miền có chính tả gần giống tên miền hợp pháp (ví dụ `gooogle.com`) để lừa người dùng truy cập nhầm vào trang giả mạo.
- **Pharming**: Hình thức lừa đảo chuyển hướng người dùng đến trang web giả mạo bằng cách thao túng DNS (qua cache poisoning, hijacking...) thay vì chỉ dùng liên kết lừa đảo như phishing thông thường.
- **Botnet (mạng máy bị chiếm quyền điều khiển)**: Tập hợp các máy bị nhiễm mã độc, được kẻ tấn công điều khiển để thực hiện các cuộc tấn công như DDoS.
- **Spoofing (giả mạo)**: Hành vi giả mạo địa chỉ IP nguồn hoặc thông tin gói tin để che giấu danh tính thật của kẻ tấn công.

---

## Chương 4: Biện pháp giảm thiểu tấn công DNS

- **Patch / Update (cập nhật bản vá)**: Việc cập nhật phần mềm máy chủ DNS (ví dụ BIND) lên phiên bản mới nhất để khắc phục các lỗ hổng đã biết.
- **MFA – Multi-Factor Authentication (Xác thực đa yếu tố)**: Phương thức xác thực yêu cầu nhiều hơn một yếu tố (mật khẩu, mã OTP, sinh trắc học...) để tăng cường bảo mật truy cập hệ thống quản trị DNS.
- **DNSSEC – Domain Name System Security Extensions**: Bộ phần mở rộng bảo mật cho DNS, sử dụng chữ ký số (digital signature) để xác thực nguồn gốc và tính toàn vẹn của dữ liệu DNS, giúp chống cache poisoning và spoofing.
- **Tách biệt máy chủ DNS (Split-horizon / Separation)**: Triển khai riêng các máy chủ DNS nội bộ (internal) và bên ngoài (external/public) để hạn chế lộ thông tin và giảm bề mặt tấn công.
- **Zone audit (kiểm tra vùng DNS)**: Quá trình rà soát lại các bản ghi trong zone file để phát hiện bản ghi dư thừa, lỗi thời hoặc bị chèn trái phép.
- **Version hiding (ẩn phiên bản BIND)**: Cấu hình máy chủ DNS để không tiết lộ thông tin phiên bản phần mềm, tránh kẻ tấn công nhắm mục tiêu khai thác lỗ hổng theo phiên bản.
- **Zone transfer restriction (giới hạn truy cập vùng DNS / AXFR restriction)**: Hạn chế chỉ cho các máy chủ được tin cậy thực hiện sao chép dữ liệu vùng (zone transfer), tránh lộ toàn bộ cấu trúc DNS.
- **Recursive query restriction (tắt/giới hạn chức năng đệ quy DNS)**: Cấu hình máy chủ chỉ trả lời truy vấn đệ quy cho các client được phép, ngăn việc bị lợi dụng làm "open resolver" trong tấn công khuếch đại.
- **Rate limiting / Anti-DDoS service (dịch vụ hạn chế tấn công DDoS)**: Sử dụng các giải pháp giới hạn tốc độ truy vấn hoặc dịch vụ chuyên biệt (CDN, Anti-DDoS) để giảm tác động của lưu lượng tấn công.
- **Network monitoring (giám sát lưu lượng mạng)**: Theo dõi liên tục lưu lượng và log truy vấn DNS để phát hiện sớm các dấu hiệu bất thường hoặc tấn công đang diễn ra.

---

> *Ghi chú: Bảng thuật ngữ có thể bổ sung/chỉnh sửa khi các chương được viết chi tiết hơn, đặc biệt ở Chương 3 và Chương 4 nơi mỗi thành viên có thể thêm thuật ngữ riêng theo nguồn tài liệu tham khảo của mình.*