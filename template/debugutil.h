#pragma once
#include <bits/stdc++.h>

namespace __DEBUG_UTIL__ {
template <typename T>
concept is_iterable = requires(T&& x) {
    begin(x);
    end(x);
    size(x);
} && !std::is_same_v<std::remove_cvref_t<T>, std::string>;
inline void print(const char* x) {
    std::cerr << x;
}
inline void print(char x) {
    std::cerr << "\'" << x << "\'";
}
inline void print(bool x) {
    std::cerr << (x ? "T" : "F");
}
inline void print(std::__cxx1998::_Bit_reference x) {
    std::cerr << (x ? "T" : "F");
}
inline void print(std::string x) {
    std::cerr << "\"" << x << "\"";
}

template <typename T>
void print(T&& x) {
    if constexpr (is_iterable<T>) /* Every iterable Ever */
        if (size(x))
            if constexpr (is_iterable<decltype(*(begin(x)))>) {
                int f = 0;
                std::cerr << "\n~~~~~\n";
                for (auto&& i : x) {
                    std::cerr << std::setw(2) << std::left << f++, print(i), std::cerr << "\n";
                }
                std::cerr << "~~~~~\n";
            } else {
                int f = 0;
                std::cerr << "{";
                for (auto&& i : x)
                    std::cerr << (f++ ? "," : ""), print(i);
                std::cerr << "}";
            }
        else
            std::cerr << "{}";
    else if constexpr (requires(T&& xt) { xt.pop(); }) /* Stacks, Priority Queues, Queues */
    {
        T temp = x;
        int f = 0;
        std::cerr << "{";
        if constexpr (requires(T&& xt) { xt.top(); })
            while (!temp.empty())
                std::cerr << (f++ ? "," : ""), print(temp.top()), temp.pop();
        else
            while (!temp.empty())
                std::cerr << (f++ ? "," : ""), print(temp.front()), temp.pop();
        std::cerr << "}";
    } else if constexpr (requires(T&& xt) {
                             xt.first;
                             xt.second;
                         }) /* Pair */
    {
        std::cerr << '(', print(x.first), std::cerr << ',', print(x.second), std::cerr << ')';
    } else if constexpr (requires(T&& xt) { get<0>(xt); }) /* Tuple */
    {
        int f = 0;
        std::cerr << '(', apply([&f](auto... args) { ((std::cerr << (f++ ? "," : ""), print(args)), ...); }, x);
        std::cerr << ')';
    } else
        std::cerr << x;
}
template <typename T, typename... V>
void printer(const char* names, T&& head, V&&... tail) {
    int i = 0;
    for (size_t bracket = 0; names[i] != '\0' and (names[i] != ',' or bracket != 0); i++)
        if (names[i] == '(' or names[i] == '<' or names[i] == '{')
            bracket++;
        else if (names[i] == ')' or names[i] == '>' or names[i] == '}')
            bracket--;
    std::cerr.write(names, i) << " = ";
    print(head);
    if constexpr (sizeof...(tail))
        std::cerr << " ||", printer(names + i + 1, tail...);
    else
        std::cerr << "]\n"
                  << "\033[0m";
}
template <typename T>
void printerArr(const char* name, T arr[], size_t N) {
    std::cerr << name << " = {";
    for (size_t i = 0; i < N; i++)
        std::cerr << (i ? "," : ""), print(arr[i]);
    std::cerr << "}";
    std::cerr << "]\n"
              << "\033[0m";
}

}

#define debug(...) std::cerr << "\033[1;35m" << __LINE__ << ": [", __DEBUG_UTIL__::printer(#__VA_ARGS__, __VA_ARGS__);
#define debugArr(arr, n) std::cerr << "\033[1;35m" << __LINE__ << ": [", __DEBUG_UTIL__::printerArr(#arr, arr, n) << "\033[0m";
