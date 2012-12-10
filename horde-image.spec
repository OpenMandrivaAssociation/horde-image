%define prj    Horde_Image

%define xmldir  %{_var}/lib/pear
%define peardir %(pear config-get php_dir 2> /dev/null)

Name:          horde-image
Version:       0.0.2
Release:       %mkrel 3
Summary:       Horde Image API
License:       LGPL
Group:         Networking/Mail
Url:           http://pear.horde.org/index.php?package=%{prj}
Source0:       %{prj}-%{version}.tgz
BuildArch:     noarch
Requires(pre): php-pear
Requires:      php-pear
Requires:      php-pear-channel-horde
Requires:      php-pear-XML_SVG
Requires:      horde-util
BuildRequires: php-pear
BuildRequires: php-pear-channel-horde


%description
This package provides an Image utility API, with backends for:
 * GD
 * GIF
 * PNG
 * SVG
 * SWF
 * ImageMagick convert command line tool

%prep
%setup -q -n %{prj}-%{version}

%build
%__mv ../package*.xml .

%install
pear install --packagingroot %{buildroot} --nodeps package.xml

%__rm -rf %{buildroot}/%{peardir}/.{filemap,lock,registry,channels,depdb,depdblock}

%__mkdir_p %{buildroot}%{xmldir}
%__cp package.xml %{buildroot}%{xmldir}/%{prj}.xml

# make some directories
install -d %{buildroot}/usr/share/pear/tests/Horde_Image/Image/


#move some files that should be somewhere else

mv %{buildroot}/usr/share/pear/tests/Horde_Image/tests/gd.php %{buildroot}/usr/share/pear/tests/Horde_Image/Image/gd.php
mv %{buildroot}/usr/share/pear/tests/Horde_Image/tests/im.php %{buildroot}/usr/share/pear/tests/Horde_Image/Image/im.php
mv %{buildroot}/usr/share/pear/tests/Horde_Image/tests/svg.php %{buildroot}/usr/share/pear/tests/Horde_Image/Image/svg.php
mv %{buildroot}/usr/share/pear/tests/Horde_Image/tests/swf.php %{buildroot}/usr/share/pear/tests/Horde_Image/Image/swf.php
rm -r %{buildroot}/usr/share/pear/tests/Horde_Image/tests/

%clean
%__rm -rf %{buildroot}

%post
pear install --nodeps --soft --force --register-only %{xmldir}/%{prj}.xml

%postun
if [ "$1" -eq "0" ]; then
  pear uninstall --nodeps --ignore-errors --register-only pear.horde.org/%{prj}
fi

%files
%defattr(-, root, root)
%{xmldir}/%{prj}.xml
%dir %{peardir}/Horde
%{peardir}/Horde/Image.php
%dir %{peardir}/Horde/Image
%{peardir}/Horde/Image/gd.php
%{peardir}/Horde/Image/im.php
%{peardir}/Horde/Image/png.php
%{peardir}/Horde/Image/rgb.php
%{peardir}/Horde/Image/svg.php
%{peardir}/Horde/Image/swf.php
%dir %{peardir}/tests/Horde_Image
%dir %{peardir}/tests/Horde_Image/Image
%{peardir}/tests/Horde_Image/Image/gd.php
%{peardir}/tests/Horde_Image/Image/im.php
%{peardir}/tests/Horde_Image/Image/svg.php
%{peardir}/tests/Horde_Image/Image/swf.php



%changelog
* Mon Aug 02 2010 Thomas Spuhler <tspuhler@mandriva.org> 0.0.2-3mdv2011.0
+ Revision: 564907
- Increased release for rebuild
- Increased release for rebuild

* Thu Mar 18 2010 Thomas Spuhler <tspuhler@mandriva.org> 0.0.2-2mdv2010.1
+ Revision: 524850
- increased rel version to 2

* Sun Feb 28 2010 Thomas Spuhler <tspuhler@mandriva.org> 0.0.2-1mdv2010.1
+ Revision: 512512
- import horde-image


