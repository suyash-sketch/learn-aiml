total=$(free -h | awk '/Mem:/ {print $2}')
used=$(free -h | awk '/Mem:/ {print $3}')
free=$(free -h | awk '/Mem:/ {print $4}')

echo "RAM Summary"
echo "Total: $total"
echo "Used: $used"
echo "Free: $free"
