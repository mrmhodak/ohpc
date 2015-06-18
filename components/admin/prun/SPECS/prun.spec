#-------------------------------------------------------------------------------
# Copyright (c) 2015, Intel Corporation
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#     * Redistributions of source code must retain the above copyright notice,
#       this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#     * Neither the name of Intel Corporation nor the names of its contributors
#       may be used to endorse or promote products derived from this software
#       without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#-------------------------------------------------------------------------------

%include %{_sourcedir}/FSP_macros

%define pname prun
%{!?PROJ_DELIM:%define PROJ_DELIM %{nil}}

Summary:   Convenience utility for parallel job launch
Name:      %{pname}%{PROJ_DELIM}
Version:   0.1.0
Release:   1
License:   BSD
Group:     fsp/admin
BuildArch: noarch
Source0:   %{pname}
Source1:   FSP_macros
BuildRoot: %{_tmppath}/%{pname}-%{version}-%{release}-root

%define package_target %{FSP_PUB}/%{pname}/%{version}

%description

prun provides a script-based wrapper for launching parallel jobs
within a resource manager for a variety of MPI families.

%prep


%build
# Binary pass-through - empty build section

%install

rm -rf $RPM_BUILD_ROOT

%{__mkdir} -p %{buildroot}/%{package_target}
install -D -m 0755 %SOURCE0 %{buildroot}/%{package_target}

# FSP moduelfile

%{__mkdir} -p %{buildroot}/%{FSP_MODULES}/%{pname}
%{__cat} << EOF > %{buildroot}/%{FSP_MODULES}/%{pname}/%{version}
#%Module1.0#####################################################################
proc ModulesHelp { } {

puts stderr " "
puts stderr "This module loads the prun job launch utility"
puts stderr " "
puts stderr "Version %{version}"
puts stderr " "

}

module-whatis "Name: prun job launch utility"
module-whatis "Version: %{version}"
module-whatis "Category: resource manager tools"
module-whatis "Description: job launch utility for multiple MPI families"

set     version                 %{version}

prepend-path    PATH            %{package_target}

EOF

%{__cat} << EOF > %{buildroot}/%{FSP_MODULES}/%{pname}/.version.%{version}
#%Module1.0#####################################################################
set     ModulesVersion      "%{version}"
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%post

%postun


%files
%defattr(-,root,root,-)
%{FSP_HOME}




