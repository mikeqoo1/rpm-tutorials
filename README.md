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
cp hello-world ~/rpmbuild/SOURCES/
```

2. 寫 spec 的文件

```bash
vim ~/rpmbuild/SPECS/hello.spec

Name:           myapp
Version:        1.0.0
Release:        1%{?dist}
Summary:        我的應用程式

License:        GPL
URL:            https://example.com/myapp
Source0:        myapp-1.0.0.tar.gz

BuildArch:      x86_64

%description
這是一個可以用 dnf 安裝的測試應用程式。

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}/usr/bin
cp myapp %{buildroot}/usr/bin/myapp

%files
/usr/bin/myapp

%changelog
* 測試
- 初始版本
```