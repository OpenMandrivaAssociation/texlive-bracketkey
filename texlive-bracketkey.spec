%global tl_name bracketkey
%global tl_revision 17129

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Produce bracketed identification keys
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/bracketkey
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bracketkey.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bracketkey.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides an environment bracketkey for use when producing
lists of species.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/bracketkey
%dir %{_datadir}/texmf-dist/tex/latex/bracketkey
%doc %{_datadir}/texmf-dist/doc/latex/bracketkey/Malva.pdf
%doc %{_datadir}/texmf-dist/doc/latex/bracketkey/Malva.tex
%doc %{_datadir}/texmf-dist/doc/latex/bracketkey/README
%doc %{_datadir}/texmf-dist/doc/latex/bracketkey/bracketkey.pdf
%doc %{_datadir}/texmf-dist/doc/latex/bracketkey/bracketkey.tex
%{_datadir}/texmf-dist/tex/latex/bracketkey/bracketkey.sty
