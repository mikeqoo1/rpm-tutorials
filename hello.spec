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
