# code đã sửa
# Biến toàn cục lưu tổng điểm hiện tại của khách hàng
total_points = 100

# Hàm cộng điểm thưởng
def add_reward_points(points_earned):
    global total_points
    # Cố gắng lấy tổng điểm cũ cộng thêm điểm mới
    total_points = total_points + points_earned
    print("Đã cộng thêm", points_earned, "điểm.")

# Khách mua hàng được thưởng 50 điểm
add_reward_points(50)

# In ra kết quả
print("Tổng điểm hiện tại của khách hàng:", total_points)

# biến total_points được khai báo ở dòng 2 là biến toàn cục vì nó được khai báo bên ngoài hàm
# UnboundLocalError: local variable 'total_points' referenced before assignment. Tại sao Python lại coi total_points : lỗi này xảy khi vì : khi gán total_points = total_points + points_earned như này thì biến total_points là 1 biến cục bộ 
# khi chỉ muốn đọc thay vì gán thì chương trình vẫn chạy bình thường vì sẽ lấy biến toàn cục đã khai báo bên ngoài
# cách 1 : thêm từ khóa global cho biến total_points 
# cách 2 : dùng return 
total_points = 100

def add_reward_points(current_points, points_earned):
    return current_points + points_earned

total_points = add_reward_points(total_points, 50)

print("Tổng điểm hiện tại của khách hàng:", total_points)