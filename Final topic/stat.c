#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sys/wait.h>
#include <sys/stat.h>
int main()
{
  struct stat sfile;

  //stat system call
  stat("pk3.txt", &sfile);
  
  printf("\nst_mode = %o \n", sfile.st_mode);
  printf("\nst_uid %d \n",sfile.st_uid);
  printf("\nst_blksize %ld \n",sfile.st_blksize);
  printf("\nst_gid %d \n",sfile.st_gid);
  printf("\nst_blocks %ld \n",sfile.st_blocks);
  printf("\nst_size %ld \n",sfile.st_size);
  printf("\nst_nlink %u \n",(unsigned int)sfile.st_nlink);
  return 0;
}
