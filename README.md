# rpm-tutorials

怎麼把執行檔打包成 RPM (Red Hat Package Manager) 格式，並建立一個 YUM/DNF Repository 來管理不同版本。

## 環境建立

先安裝套件

```bash
sudo dnf install -y rpm-build dnf-utils createrepo
sudo dnf install rpmdevtools
rpmdev-setuptree
```

```txt
$ tree ~/rpmbuild/
/home/<username>/rpmbuild/
|-- BUILD (放安裝過程中的紀錄)
|-- RPMS (編譯好的RPM包)
|-- SOURCES (放我們執行檔的地方 要被編譯成RPM的東西)
|-- SPECS (放 SPEC 文件包含安裝軟體的名稱、版本、作者、依賴關係、安裝路徑等等)
`-- SRPMS

5 directories, 0 files
```

## 編譯範例程式

```bash
cmake CMakeLists.txt
make
```

## 開始編譯 RPM 包

1. 先把執行檔丟到SOURCES裡

```bash
cp hello ~/rpmbuild/SOURCES/
```

2. 寫 spec 的文件

```bash
Name:           hello
Version:        1.0.0
Release:        1%{?dist}
Summary:        A simple Hello World program

License:        GPL
URL:            https://example.com/hello
Source0:        hello

BuildArch:      x86_64

%description
This is a simple Hello World program packaged as an RPM.

%prep

%build

%install
mkdir -p %{buildroot}/usr/bin
cp %{SOURCE0} %{buildroot}/usr/bin/hello

%files
/usr/bin/hello

%changelog
* Tue Feb 6 2025 mike - 1.0.0-1
- Initial package
```

3. 建立 RPM 套件

```bash
rpmbuild -ba ~/rpmbuild/SPECS/hello.spec
```

如果沒錯會產生

```bash
~/rpmbuild/RPMS/x86_64/hello-1.0.0-1.el9.x86_64.rpm
```

4. 安裝 RPM

```bash
sudo dnf install ~/rpmbuild/RPMS/x86_64/hello-1.0.0-1.el9.x86_64.rpm
```

5. 設定 DNF Repository 自己建倉庫

本地建立倉庫

建立倉庫目錄

```bash
sudo mkdir -p /var/www/html/repo
sudo cp ~/rpmbuild/RPMS/x86_64/hello-1.0.0-1.el9.x86_64.rpm /var/www/html/repo/
```

建立倉庫索引

```bash
sudo createrepo /var/www/html/repo
```

設定 dnf 存取

```bash
在 sudo vim /etc/yum.repos.d/myrepo.repo
[myrepo]
name=My Custom Repo
# baseurl=<http://your-server-ip/repo>  要架設http
baseurl=file:///var/www/html/repo # 簡易本地端
enabled=1
gpgcheck=0
```
