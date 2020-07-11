/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package af.asr.mohediploma.model;

import java.io.Serializable;
import java.util.Date;
import java.util.List;
import javax.persistence.Basic;
import javax.persistence.CascadeType;
import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.NamedQueries;
import javax.persistence.NamedQuery;
import javax.persistence.OneToMany;
import javax.persistence.OneToOne;
import javax.persistence.Table;
import javax.persistence.Temporal;
import javax.persistence.TemporalType;

/**
 *
 * @author badar
 */
@Entity
@Table(name = "auth_user")
//@NamedQueries({
//    @NamedQuery(name = "AuthUser.findAll", query = "SELECT a FROM AuthUser a")})
public class AuthUser implements Serializable {

    private static final long serialVersionUID = 1L;
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Basic(optional = false)
    @Column(name = "id")
    private Integer id;
    @Basic(optional = false)
    @Column(name = "password")
    private String password;
    @Column(name = "last_login")
    @Temporal(TemporalType.TIMESTAMP)
    private Date lastLogin;
    @Basic(optional = false)
    @Column(name = "is_superuser")
    private boolean isSuperuser;
    @Basic(optional = false)
    @Column(name = "username")
    private String username;
    @Basic(optional = false)
    @Column(name = "first_name")
    private String firstName;
    @Basic(optional = false)
    @Column(name = "last_name")
    private String lastName;
    @Basic(optional = false)
    @Column(name = "email")
    private String email;
    @Basic(optional = false)
    @Column(name = "is_staff")
    private boolean isStaff;
    @Basic(optional = false)
    @Column(name = "is_active")
    private boolean isActive;
    @Basic(optional = false)
    @Column(name = "date_joined")
    @Temporal(TemporalType.TIMESTAMP)
    private Date dateJoined;
    @OneToMany(cascade = CascadeType.ALL, mappedBy = "userId")
    private List<AuthUserUserPermissions> authUserUserPermissionsList;
    @OneToMany(mappedBy = "userId")
    private List<Blankdiploma> blankdiplomaList;
    @OneToMany(mappedBy = "userId")
    private List<Certificate> certificateList;
    @OneToMany(mappedBy = "userId")
    private List<University> universityList;
    @OneToMany(mappedBy = "userId")
    private List<Faculty> facultyList;
    @OneToOne(cascade = CascadeType.ALL, mappedBy = "userId")
    private Userfacultyrelation userfacultyrelation;
    @OneToMany(mappedBy = "userId")
    private List<Department> genericDepartmentList;
    @OneToMany(cascade = CascadeType.ALL, mappedBy = "userId")
    private List<DjangoAdminLog> djangoAdminLogList;
    @OneToMany(mappedBy = "userId")
    private List<Universitydiplomadistribution> universitydiplomadistributionList;
    @OneToMany(cascade = CascadeType.ALL, mappedBy = "userId")
    private List<AuthUserGroups> authUserGroupsList;

    public AuthUser() {
    }

    public AuthUser(Integer id) {
        this.id = id;
    }

    public AuthUser(Integer id, String password, boolean isSuperuser, String username, String firstName, String lastName, String email, boolean isStaff, boolean isActive, Date dateJoined) {
        this.id = id;
        this.password = password;
        this.isSuperuser = isSuperuser;
        this.username = username;
        this.firstName = firstName;
        this.lastName = lastName;
        this.email = email;
        this.isStaff = isStaff;
        this.isActive = isActive;
        this.dateJoined = dateJoined;
    }

    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }

    public Date getLastLogin() {
        return lastLogin;
    }

    public void setLastLogin(Date lastLogin) {
        this.lastLogin = lastLogin;
    }

    public boolean getIsSuperuser() {
        return isSuperuser;
    }

    public void setIsSuperuser(boolean isSuperuser) {
        this.isSuperuser = isSuperuser;
    }

    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }

    public String getFirstName() {
        return firstName;
    }

    public void setFirstName(String firstName) {
        this.firstName = firstName;
    }

    public String getLastName() {
        return lastName;
    }

    public void setLastName(String lastName) {
        this.lastName = lastName;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public boolean getIsStaff() {
        return isStaff;
    }

    public void setIsStaff(boolean isStaff) {
        this.isStaff = isStaff;
    }

    public boolean getIsActive() {
        return isActive;
    }

    public void setIsActive(boolean isActive) {
        this.isActive = isActive;
    }

    public Date getDateJoined() {
        return dateJoined;
    }

    public void setDateJoined(Date dateJoined) {
        this.dateJoined = dateJoined;
    }

    public List<AuthUserUserPermissions> getAuthUserUserPermissionsList() {
        return authUserUserPermissionsList;
    }

    public void setAuthUserUserPermissionsList(List<AuthUserUserPermissions> authUserUserPermissionsList) {
        this.authUserUserPermissionsList = authUserUserPermissionsList;
    }

    public List<Blankdiploma> getBlankdiplomaList() {
        return blankdiplomaList;
    }

    public void setBlankdiplomaList(List<Blankdiploma> blankdiplomaList) {
        this.blankdiplomaList = blankdiplomaList;
    }

    public List<Certificate> getCertificateList() {
        return certificateList;
    }

    public void setCertificateList(List<Certificate> certificateList) {
        this.certificateList = certificateList;
    }

    public List<University> getUniversityList() {
        return universityList;
    }

    public void setUniversityList(List<University> universityList) {
        this.universityList = universityList;
    }

    public List<Faculty> getFacultyList() {
        return facultyList;
    }

    public void setFacultyList(List<Faculty> facultyList) {
        this.facultyList = facultyList;
    }

    public Userfacultyrelation getUserfacultyrelation() {
        return userfacultyrelation;
    }

    public void setUserfacultyrelation(Userfacultyrelation userfacultyrelation) {
        this.userfacultyrelation = userfacultyrelation;
    }

    public List<Department> getGenericDepartmentList() {
        return genericDepartmentList;
    }

    public void setGenericDepartmentList(List<Department> genericDepartmentList) {
        this.genericDepartmentList = genericDepartmentList;
    }

    public List<DjangoAdminLog> getDjangoAdminLogList() {
        return djangoAdminLogList;
    }

    public void setDjangoAdminLogList(List<DjangoAdminLog> djangoAdminLogList) {
        this.djangoAdminLogList = djangoAdminLogList;
    }

    public List<Universitydiplomadistribution> getUniversitydiplomadistributionList() {
        return universitydiplomadistributionList;
    }

    public void setUniversitydiplomadistributionList(List<Universitydiplomadistribution> universitydiplomadistributionList) {
        this.universitydiplomadistributionList = universitydiplomadistributionList;
    }

    public List<AuthUserGroups> getAuthUserGroupsList() {
        return authUserGroupsList;
    }

    public void setAuthUserGroupsList(List<AuthUserGroups> authUserGroupsList) {
        this.authUserGroupsList = authUserGroupsList;
    }

    @Override
    public int hashCode() {
        int hash = 0;
        hash += (id != null ? id.hashCode() : 0);
        return hash;
    }

    @Override
    public boolean equals(Object object) {
        // TODO: Warning - this method won't work in the case the id fields are not set
        if (!(object instanceof AuthUser)) {
            return false;
        }
        AuthUser other = (AuthUser) object;
        if ((this.id == null && other.id != null) || (this.id != null && !this.id.equals(other.id))) {
            return false;
        }
        return true;
    }

    @Override
    public String toString() {
        return "af.asr.mohediploma.model.AuthUser[ id=" + id + " ]";
    }
    
}
