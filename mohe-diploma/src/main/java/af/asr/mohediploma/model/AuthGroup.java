/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package af.asr.mohediploma.model;

import java.io.Serializable;
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
import javax.persistence.Table;

/**
 *
 * @author badar
 */
@Entity
@Table(name = "auth_group")
//@NamedQueries({
//    @NamedQuery(name = "AuthGroup.findAll", query = "SELECT a FROM AuthGroup a")})
public class AuthGroup implements Serializable {

    private static final long serialVersionUID = 1L;
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Basic(optional = false)
    @Column(name = "id")
    private Integer id;
    @Basic(optional = false)
    @Column(name = "name")
    private String name;
    @OneToMany(cascade = CascadeType.ALL, mappedBy = "groupId")
    private List<AuthGroupPermissions> authGroupPermissionsList;
    @OneToMany(cascade = CascadeType.ALL, mappedBy = "groupId")
    private List<AuthUserGroups> authUserGroupsList;

    public AuthGroup() {
    }

    public AuthGroup(Integer id) {
        this.id = id;
    }

    public AuthGroup(Integer id, String name) {
        this.id = id;
        this.name = name;
    }

    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<AuthGroupPermissions> getAuthGroupPermissionsList() {
        return authGroupPermissionsList;
    }

    public void setAuthGroupPermissionsList(List<AuthGroupPermissions> authGroupPermissionsList) {
        this.authGroupPermissionsList = authGroupPermissionsList;
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
        if (!(object instanceof AuthGroup)) {
            return false;
        }
        AuthGroup other = (AuthGroup) object;
        if ((this.id == null && other.id != null) || (this.id != null && !this.id.equals(other.id))) {
            return false;
        }
        return true;
    }

    @Override
    public String toString() {
        return "af.asr.mohediploma.model.AuthGroup[ id=" + id + " ]";
    }
    
}
