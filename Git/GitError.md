<h1>21/07/14</h1>



+ 파일 2개 commit
+ 1개 커밋 메세지 바꾸려고 전체 커밋을 취소함 (cmd에서 git revert head^ )
+ 스테이지에 올라가지 않고 2개 파일자체가 삭제됨 
+ 이전 브랜치에서 파일 복원해서 petch, pull, push 시도 - 모두 에러 (SourceTree)
 
<u>

=> __remote repository에서 파일 삭제하고 진행하니 해결됨__ (git 홈페이지)

</u>

<br>

<h1>21/07/17 - ErMg 폴더에서 이동</h1>


* 새 저장소 만들었는데 브랜치 생성이 안됨 

<u>

=> __새로 커밋하면 자동 생성__

</u>

<br>

<h1>21/07/18</h1>

* cmd에서 git --help로 보는 중에 escape 안될 떄 

<u>

=> __Q로 esacape__

</u>

<h1>21/07/20</h1>

* cmd에서 git push 입력 후 에러 메시지 출력
  
* C:\GIT\Error>git push
To https://github.com/kingdomunder/Error
 ! [rejected]        main -> main (non-fast-forward)
error: failed to push some refs to 'https://github.com/kingdomunder/Error'
hint: Updates were rejected because the tip of your current branch is behind
hint: its remote counterpart. Integrate the remote changes (e.g.
hint: 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.

* pull 하면 clean your repository 에러 출력

=> <u>__소스트리에서 강제푸쉬__</u> - 소스트리 이외에서 강제푸쉬 하는 방법 알아보기 