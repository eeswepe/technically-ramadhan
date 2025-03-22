#include <deque>
#include <iostream>

static int dblLinear(int n) {
  std::deque<int> y_res, z_res;
  int ans = 1;

  for (int i = 0; i < n; i++) {
    y_res.push_back(2 * ans + 1);
    z_res.push_back(3 * ans + 1);

    if (y_res.front() < z_res.front()) {
      ans = y_res.front();
      y_res.pop_front();
    } else if (z_res.front() < y_res.front()) {
      ans = z_res.front();
      z_res.pop_front();
    } else {
      ans = y_res.front();
      y_res.pop_front();
      z_res.pop_front();
    }
  }
  return ans;
}

int main() {
  std::cout << dblLinear(10) << std::endl;
  return 0;
}
