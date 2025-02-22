#pragma once

#include <bitset>
#include <iostream>
#include <string>
#include <tuple>
#include <vector>
// === Debug macro starts here ===

namespace std {
template <typename A, typename B>
std::string to_string(std::pair<A, B> p);
template <typename A, typename B, typename C>
std::string to_string(std::tuple<A, B, C> p);
template <typename A, typename B, typename C, typename D>
std::string to_string(std::tuple<A, B, C, D> p);
inline std::string to_string(const std::string &s) { return '"' + s + '"'; }
inline std::string to_string(const char *s) { return to_string((std::string)s); }
inline std::string to_string(bool b) { return (b ? "true" : "false"); }
inline std::string to_string(std::vector<bool> v) {
    bool first = true;
    std::string res = "{";
    for (int i = 0; i < static_cast<int>(v.size()); i++) {
        if (!first) {
            res += ", ";
        }
        first = false;
        res += to_string(v[i]);
    }
    res += "}";
    return res;
}
template <size_t N>
std::string to_string(std::bitset<N> v) {
    std::string res = "";
    for (size_t i = 0; i < N; i++) {
        res += static_cast<char>('0' + v[i]);
    }
    return res;
}
template <typename A>
std::string to_string(A v) {
    bool first = true;
    std::string res = "{";
    for (const auto &x : v) {
        if (!first) {
            res += ", ";
        }
        first = false;
        res += to_string(x);
    }
    res += "}";
    return res;
}
template <typename A, typename B>
std::string to_string(std::pair<A, B> p) { return "(" + to_string(p.first) + ", " + to_string(p.second) + ")"; }
template <typename A, typename B, typename C>
std::string to_string(std::tuple<A, B, C> p) { return "(" + to_string(std::get<0>(p)) + ", " + to_string(std::get<1>(p)) + ", " + to_string(std::get<2>(p)) + ")"; }
template <typename A, typename B, typename C, typename D>
std::string to_string(std::tuple<A, B, C, D> p) { return "(" + to_string(std::get<0>(p)) + ", " + to_string(std::get<1>(p)) + ", " + to_string(std::get<2>(p)) + ", " + to_string(std::get<3>(p)) + ")"; }
}  // namespace std
inline void debug_out() { std::cerr << "\033[0m"
                                    << "\n"; }
template <typename Head, typename... Tail>
void debug_out(Head H, Tail... T) {
    std::cerr << " " << std::to_string(H);
    debug_out(T...);
}

#define debug(...) std::cerr << "\033[1;31mLINE(" << __LINE__ << ") [" << __FUNCTION__ << "] -> " \
                             << "[" << #__VA_ARGS__ << "]:",                                    \
                   debug_out(__VA_ARGS__)
