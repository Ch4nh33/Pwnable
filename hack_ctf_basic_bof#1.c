int __cdecl main(int argc, const char **argv, const char **envp)
{
  char s; // [esp+4h] [ebp-34h]
  int v5; // [esp+2Ch] [ebp-Ch]

  v5 = 67305985;
  fgets(&s, 45, stdin);
  printf("\n[buf]: %s\n", &s);
  printf("[check] %p\n", v5);
  if ( v5 != 67305985 && v5 != -559038737 )
    puts("\nYou are on the right way!");
  if ( v5 == -559038737 )
  {
    puts("Yeah dude! You win!\nOpening your shell...");
    system("/bin/dash");
    puts("Shell closed! Bye.");
  }
  return 0;
}
