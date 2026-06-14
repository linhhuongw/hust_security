# CHƯƠNG 2: LỖ HỔNG BẢO MẬT CỦA DNS

## 2.1. Lỗ hổng bảo mật của DNS

**Lỗ hổng bảo mật (Vulnerability)** là điểm yếu tồn tại trong thiết kế, cấu hình hoặc cách triển khai của một giao thức hay hệ thống, có thể bị lợi dụng để gây ra hậu quả ngoài mong muốn. Đối với DNS, phần lớn các lỗ hổng không xuất phát từ lỗi lập trình đơn lẻ mà bắt nguồn từ **bản chất thiết kế ban đầu của giao thức**: DNS được phát triển từ những năm 1980, vào thời điểm bảo mật chưa phải là ưu tiên hàng đầu, mục tiêu chính là **tốc độ phân giải nhanh** và **khả năng mở rộng trên quy mô toàn cầu**.

Ba nhóm lỗ hổng cốt lõi thường được nhắc đến gồm:

- **Thiếu xác thực nguồn**: Bên nhận một phản hồi DNS thường không có cách nào kiểm chứng chắc chắn rằng phản hồi đó thực sự đến từ máy chủ hợp lệ.
- **Thiếu mã hóa**: Dữ liệu truy vấn và phản hồi được truyền dưới dạng **plaintext**, dễ bị quan sát hoặc can thiệp trên đường truyền.
- **Cơ chế cache**: Việc lưu tạm kết quả phân giải giúp tăng hiệu năng nhưng cũng tạo ra **bề mặt tấn công** — nếu dữ liệu sai bị đưa vào cache, nó sẽ tiếp tục được sử dụng cho đến khi hết TTL.

Đây chính là nền tảng lý thuyết để hiểu vì sao các kiểu tấn công ở Chương 3 (cache poisoning, spoofing, hijacking...) đều có thể xảy ra.

## 2.2. Khai thác (Exploit) lỗ hổng DNS

**Exploit (khai thác)** là hành động, kỹ thuật hoặc công cụ cụ thể lợi dụng một lỗ hổng để đạt được mục đích của kẻ tấn công — có thể là **đánh cắp dữ liệu, chuyển hướng người dùng, hoặc làm gián đoạn dịch vụ**.

Điểm quan trọng cần phân biệt: *lỗ hổng* là điều kiện tồn tại sẵn (ví dụ DNS không xác thực nguồn phản hồi), còn *exploit* là bước biến điều kiện đó thành một cuộc tấn công thực sự (ví dụ gửi hàng loạt phản hồi giả mạo để "đoán đúng" Transaction ID trước khi phản hồi hợp lệ đến). Một lỗ hổng có thể tồn tại trong nhiều năm mà không gây hại nếu không có exploit tương ứng, nhưng **khi exploit được công khai (zero-day), thời gian từ lúc phát hiện đến lúc bị lợi dụng có thể chỉ tính bằng giờ**.

## 2.3. Giao thức UDP/TCP trong DNS

DNS hoạt động chủ yếu trên **UDP, cổng 53**, vì UDP không cần thiết lập kết nối (no handshake), giúp truy vấn diễn ra **nhanh và ít tốn tài nguyên** — phù hợp với khối lượng truy vấn khổng lồ trên Internet.

Tuy nhiên, đây cũng là **nguồn gốc của nhiều lỗ hổng**: vì UDP không có cơ chế kiểm tra trạng thái kết nối, kẻ tấn công có thể dễ dàng **giả mạo địa chỉ IP nguồn (spoofing)** và gửi gói tin mà bên nhận khó phát hiện ra sự giả mạo. Đặc điểm này là điều kiện tiên quyết cho các kỹ thuật như **DNS amplification** và **cache poisoning** ở Chương 3.

TCP (cũng trên cổng 53) chỉ được dùng trong một số trường hợp đặc biệt — như **zone transfer (AXFR)** giữa các máy chủ DNS, hoặc khi kích thước phản hồi vượt quá giới hạn của UDP. TCP an toàn hơn về mặt xác thực kết nối, nhưng nếu **không được giới hạn truy cập đúng cách**, zone transfer qua TCP có thể bị lợi dụng để **lấy toàn bộ dữ liệu của một vùng DNS**.

## 2.4. Plaintext – Truyền dữ liệu không mã hóa

Theo thiết kế truyền thống, **toàn bộ truy vấn và phản hồi DNS được truyền dưới dạng văn bản rõ (plaintext)**, không có lớp mã hóa bảo vệ. Điều này dẫn đến hai rủi ro chính:

- **Nghe trộm (eavesdropping)**: Bất kỳ ai có quyền quan sát lưu lượng trên đường truyền (ISP, mạng Wi-Fi công cộng, kẻ tấn công nằm giữa đường truyền...) đều có thể đọc được nội dung truy vấn — biết được người dùng đang truy cập tên miền nào.
- **Sửa đổi dữ liệu (tampering)**: Vì không có cơ chế xác thực tính toàn vẹn, dữ liệu có thể bị **chặn và thay đổi** trên đường truyền mà bên nhận không nhận ra — đây chính là cơ sở cho tấn công **Man-in-the-Middle (MITM)** ở Chương 3.

Đặc điểm "không mã hóa, không xác thực" này là lý do các giải pháp như **DNSSEC** (xác thực, đảm bảo toàn vẹn) và **DoH/DoT – DNS over HTTPS/TLS** (mã hóa đường truyền) được phát triển sau này, sẽ được đề cập ở Chương 4.

## 2.5. Vì sao DNS có lỗ hổng bảo mật nhưng vẫn được sử dụng rộng rãi?

Dù tồn tại nhiều lỗ hổng nêu trên, DNS vẫn là **hạ tầng nền tảng không thể thay thế** của Internet, vì các lý do sau:

- **Tính phổ quát và tương thích ngược**: Hầu hết thiết bị, hệ điều hành và ứng dụng trên toàn cầu đều dựa vào DNS truyền thống; thay đổi giao thức gốc đòi hỏi sự đồng thuận và triển khai đồng bộ ở quy mô toàn cầu — gần như không khả thi trong thời gian ngắn.
- **Hiệu năng vượt trội**: Cơ chế UDP + cache giúp DNS trả kết quả trong vài **milliseconds**, điều mà các giao thức an toàn hơn (yêu cầu mã hóa, xác thực) khó đạt được nếu áp dụng đại trà ngay từ đầu.
- **Chi phí chuyển đổi cao**: Triển khai các lớp bảo mật bổ sung (DNSSEC, DoH/DoT) đòi hỏi **cập nhật hạ tầng, cấu hình lại hệ thống và đào tạo quản trị viên**, trong khi lỗ hổng không phải lúc nào cũng bị khai thác trên thực tế.
- **Giải pháp bảo mật bổ sung đã tồn tại**: Thay vì thay thế DNS, ngành công nghiệp chọn cách **vá và mở rộng** giao thức gốc (DNSSEC, rate limiting, monitoring...) — vừa giữ được tính tương thích, vừa giảm thiểu rủi ro, sẽ được trình bày chi tiết ở Chương 4.

> **Tóm lại**: DNS giống như một "con đường cao tốc" được xây từ lâu, lưu lượng khổng lồ và không thể đóng để xây lại — giải pháp khả thi là **bổ sung biển báo, camera giám sát và trạm kiểm soát** (các lớp bảo mật bổ sung) trên nền đường cũ, hơn là phá đi xây mới.