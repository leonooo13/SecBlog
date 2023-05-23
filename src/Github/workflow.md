<h1 align='center'> Github workflow 使用指南</h1>

一些基本字段。

1. name
name字段是 workflow 的名称。如果省略该字段，默认为当前 workflow 的文件名。
```
name: GitHub Actions Test
```
2. on
   
on字段指定触发 workflow 的条件，通常是某些事件。

on: push
上面代码指定，push事件触发 workflow。

on字段也可以是事件的数组。

`on: [push, pull_request]`
上面代码指定，push事件或pull_request事件都可以触发 workflow。

完整的事件列表，请查看官方文档。除了代码库事件，GitHub Actions 也支持外部事件触发，或者定时运行。

1. on. .
指定触发事件时，可以限定分支或标签。

on:
  push:
    branches:
      - master
上面代码指定，只有master分支发生push事件时，才会触发 workflow。

4. jobs..name
workflow 文件的主体是jobs字段，表示要执行的一项或多项任务。

jobs字段里面，需要写出每一项任务的job_id，具体名称自定义。job_id里面的name字段是任务的说明。
```
jobs:
  my_first_job:
    name: My first job
  my_second_job:
    name: My second job
```
上面代码的jobs字段包含两项任务，job_id分别是my_first_job和my_second_job。

5. jobs..needs
needs字段指定当前任务的依赖关系，即运行顺序。
```
jobs:
  job1:
  job2:
    needs: job1
  job3:
    needs: [job1, job2]
```
上面代码中，job1必须先于job2完成，而job3等待job1和job2的完成才能运行。因此，这个 workflow 的运行顺序依次为：job1、job2、job3。

6. jobs..runs-on
runs-on字段指定运行所需要的虚拟机环境。它是必填字段。目前可用的虚拟机如下。
````
ubuntu-latest，ubuntu-18.04或ubuntu-16.04
windows-latest，windows-2019或windows-2016
macOS-latest或macOS-10.14
````
下面代码指定虚拟机环境为ubuntu-18.04。
```
runs-on: ubuntu-18.04
```
7. jobs..steps
steps字段指定每个 Job 的运行步骤，可以包含一个或多个步骤。每个步骤都可以指定以下三个字段。

jobs.<job_id>.steps.name：步骤名称。

jobs.<job_id>.steps.run：该步骤运行的命令或者 action。

jobs.<job_id>.steps.env：该步骤所需的环境变量。

下面是一个完整的 workflow 文件的范例。
```
name: Greeting from Mona
on: push

jobs:
  my-job:
    name: My Job
    runs-on: ubuntu-latest
    steps:
    - name: Print a greeting
      env:
        MY_VAR: Hi there! My name is
        FIRST_NAME: Mona
        MIDDLE_NAME: The
        LAST_NAME: Octocat
      run: |
        echo $MY_VAR $FIRST_NAME $MIDDLE_NAME $LAST_NAME.
```
上面代码中，steps字段只包括一个步骤。该步骤先注入四个环境变量，然后执行一条 Bash 命令，当代码push时触发这个workflow。

运行测试

先来看看项目目录：
```
GithubActionLearn/
|-- .github
|   -- workflows
|       -- first.yaml          // yaml文件
|-- README.md
-- learn
    |-- learn_01.md
    -- learn_02.md
```