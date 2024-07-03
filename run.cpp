#include <stdio.h>
#include <windows.h>
#include <string.h>

int main(int argc, char** argv)
{
    system("taskkill /f /im python.exe");
    system("python main.py");
    return 0;
}